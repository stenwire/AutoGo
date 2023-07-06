from django.shortcuts import get_object_or_404
from rest_framework import serializers

from ..models.brands import Brand
from ..models.cars import Cars
from ..models.categories import Category
from ..models.features import Features
from ..models.rented_cars import RentedCars
from ..models.reviews import Reviews
from .reviews import ReviewsSerializer


class CarsSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.id")
    features = serializers.SlugRelatedField(
        many=True, queryset=Features.objects.all(), slug_field="name"
    )
    brand = serializers.SlugRelatedField(
        queryset=Brand.objects.all(), slug_field="name"
    )
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(), slug_field="name"
    )
    reviews = ReviewsSerializer(many=True, read_only=True)

    class Meta:
        model = Cars
        fields = [
            "id",
            "user",
            "name",
            "description",
            "price",
            "brand",
            "category",
            "features",
            "pickup_time",
            "dropoff_time",
            "pickup_location",
            "dropoff_location",
            "available",
            "reviews",
            "available",
        ]
        read_only_fields = ("id",)
        # extra_kwargs = {"reviews": {"required": False, "allow_null": True}}
        # lookup_field = "id"
        # extra_kwargs = {
        #     "url": {"lookup_field": ("id")},
        # }


class CarRentalSerializer(serializers.ModelSerializer):
    # price = serializers.SlugRelatedField(
    #     many=True,
    #     queryset=Cars.objects.all(),
    #     slug_field='price'
    # )
    class Meta:
        model = RentedCars
        fields = ("__all__",)
        read_only_fields = ("id",)
        lookup_field = "id"
        extra_kwargs = {
            "url": {"lookup_field": ("id")},
        }

    def create(self, validated_data):
        return RentedCars.objects.create(**validated_data)


class RentedCarsSerializer(serializers.ModelSerializer):
    cars = CarsSerializer(
        # many=True,
        read_only=True,
        # slug_field='name'
    )

    class Meta:
        model = RentedCars
        fields = "__all__"
        # read_only_fields = ("id",)
        # fields = ("car", "tracking_number",)

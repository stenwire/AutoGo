from django.shortcuts import get_object_or_404
from rest_framework import serializers

from ..models.brands import Brand
from ..models.cars import Cars
from ..models.categories import Category
from ..models.features import Features
from ..models.rented_cars import RentedCars
from ..models.reviews import Reviews


class FeaturesSerializer(serializers.ModelSerializer):
    cars = serializers.SlugRelatedField(many=True, read_only=True, slug_field="name")

    class Meta:
        model = Features
        read_only_fields = ("id",)
        fields = "__all__"

from authme.permissions import IsAdminUserOrReadOnly, ProtectAllMethods
from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models.brands import Brand
from ..models.cars import Cars
from ..models.categories import Category
from ..models.features import Features
from ..models.rented_cars import RentedCars
from ..models.reviews import Reviews
from ..serializers.brands import BrandSerializer
from ..serializers.cars import CarRentalSerializer, CarsSerializer, RentedCarsSerializer
from ..serializers.categories import CategorySerializer
from ..serializers.features import FeaturesSerializer
from ..serializers.reviews import ReviewsSerializer


class ReviewsView(generics.ListCreateAPIView):
    permission_classes = []
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer


class ReviewList(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer

    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        serializer.save()


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [ProtectAllMethods]
    serializer_class = ReviewsSerializer

    def get_queryset(self):
        car_id = self.kwargs.get("car_id")
        review_id = self.kwargs.get("pk")
        try:
            car = Cars.objects.get(id=car_id)
            return Reviews.objects.filter(id=review_id, car=car)
        except Cars.DoesNotExist:
            return Reviews.objects.none()

    def get_object(self):
        queryset = self.get_queryset()
        obj = generics.get_object_or_404(queryset)
        return obj

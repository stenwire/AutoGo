from django.shortcuts import get_object_or_404

# from requests import Response
from rest_framework import generics, permissions, status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from authme.permissions import IsAdminUserOrReadOnly

from ..models.brands import Brand
from ..models.cars import Cars
from ..models.categories import Category
from ..models.features import Features
from ..models.rented_cars import RentedCars
from ..models.reviews import Reviews
from ..serializers.brands import BrandSerializer
from ..serializers.categories import CategorySerializer
from ..serializers.features import FeaturesSerializer
from ..serializers.reviews import ReviewsSerializer


class BrandView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated & IsAdminUserOrReadOnly]
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

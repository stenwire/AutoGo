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
from ..serializers.cars import CarRentalSerializer, CarsSerializer, RentedCarsSerializer
from ..serializers.categories import CategorySerializer
from ..serializers.features import FeaturesSerializer
from ..serializers.reviews import ReviewsSerializer


class FeaturesView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated & IsAdminUserOrReadOnly]
    queryset = Features.objects.all()
    serializer_class = FeaturesSerializer
    # filter_backends = (filters.DjangoFilterBackend,)
    # filter_class = LibraryFilter

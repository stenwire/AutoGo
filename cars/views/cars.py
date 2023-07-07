from django.shortcuts import get_object_or_404
from rest_framework import filters, generics, permissions, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView

from authme.permissions import IsAdminUserOrReadOnly
from utils.filters import CarsFilter

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

# class CarsView(generics.ListCreateAPIView):
#     permission_classes = []
#     queryset = Cars.objects.all()
#     # queryset = Cars.objects.filter(available=True)
#     serializer_class = CarsSerializer

# class CarList(generics.ListCreateAPIView):
#     permission_classes = []
#     queryset = Cars.objects.all()
#     serializer_class = CarsSerializer


# class CarList(viewsets.ModelViewSet):
#     permission_classes = [permissions.IsAuthenticated]
#     # queryset = Cars.objects.filter(available=True)
#     serializer_class = CarsSerializer

#     def get_queryset(self):
#         if self.request.method == 'GET':
#             return Cars.objects.filter(available=True)
#         return Cars.objects.all()

#     @action(detail=True, methods=["get"])
#     def reviews(self, request, pk=None):
#         car = self.get_object()
#         reviews = car.get_reviews()
#         serializer = ReviewsSerializer(reviews, many=True)
#         return Response(serializer.data)

#     @action(detail=True, methods=["post"])
#     def add_review(self, request, pk=None):
#         car = self.get_object()
#         serializer = ReviewsSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(user=request.user, car=car)
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)

#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)


# class CarDetail(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = [permissions.IsAuthenticated]
#     queryset = Cars.objects.all()
#     serializer_class = CarsSerializer


class CarListCreate(generics.ListCreateAPIView):
    queryset = Cars.objects.all()
    serializer_class = CarsSerializer
    filter_backends = (filters.BaseFilterBackend,)
    filterset_class = CarsFilter

    def filter_queryset(self, queryset):
        if self.filterset_class:
            queryset = self.filterset_class(
                data=self.request.query_params, queryset=queryset, request=self.request
            ).qs
        return queryset

    def get_queryset(self):
        # pickup_time = self.request.GET.get('pickup_time')
        # print(f'pickup_time: {pickup_time}')
        if self.request.method == "GET":
            return Cars.objects.filter(available=True)
        return Cars.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CarRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Cars.objects.all()
    serializer_class = CarsSerializer

    def get_queryset(self):
        if self.request.method == "GET":
            return Cars.objects.filter(available=True)
        return Cars.objects.all()


class RentedCarsView(generics.ListAPIView):
    permission_classes = [IsAdminUserOrReadOnly]
    serializer_class = RentedCarsSerializer

    def get_queryset(self):
        return RentedCars.objects.all()


class UserRentedCarsView(generics.ListAPIView):
    permission_classes = [IsAdminUserOrReadOnly]
    serializer_class = RentedCarsSerializer

    def get_queryset(self):
        return Cars.objects.filter(booked_by=self.request.user)


class CarRentView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CarsSerializer

    def post(self, request, car_id):
        # dropoff_time = request.GET.get('dropoff_time')
        # pickup_time = request.GET.get('pickup_time')

        try:
            car = Cars.objects.get(pk=car_id, available=True)
            car.available = False
            car.booked_by = request.user

            # if pickup_time is not None:
            #     if pickup_time != car.pickup_time:
            #         car.pickup_time = pickup_time
            # if dropoff_time is not None:
            #     car.dropoff_time = dropoff_time

            car.save()
            # rented_car = RentedCars.objects.create(car=car, user=request.user)
            rented_car = RentedCars.objects.create(car=car)
            serializer = CarsSerializer(car)
            message = "Car booked successfully. Proceed to the pickup location."
            return Response({"car": serializer.data, "message": message})
        except Cars.DoesNotExist:
            return Response({"error": "Car not found."}, status=404)

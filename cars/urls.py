from django.urls import include, path

from .views.brands import BrandView
from .views.cars import (
    CarListCreate,
    CarRentView,
    CarRetrieveUpdateDestroy,
    RentedCarsView,
)
from .views.categories import CategoryView
from .views.features import FeaturesView
from .views.reviews import ReviewDetail, ReviewListCreate

urlpatterns = [
    path("features/", FeaturesView.as_view(), name="features-list-create"),
    path("categories/", CategoryView.as_view(), name="category-list-create"),
    path("brands/", BrandView.as_view(), name="brand-list-create"),
    # --------------------
    path("cars/<car_id>/rent/", CarRentView.as_view(), name="book-car"),
    path("rented-cars/", RentedCarsView.as_view(), name="booked-cars"),
    # -----------------------
    path("cars/", CarListCreate.as_view(), name="car-list"),
    path(
        "cars/<pk>/",
        CarRetrieveUpdateDestroy.as_view(),
        name="car-detail-update-delete",
    ),
    path(
        "cars/<car_id>/reviews/", ReviewListCreate.as_view(), name="review-list-create"
    ),
    path("cars/<car_id>/reviews/<pk>/", ReviewDetail.as_view(), name="review-detail"),
]

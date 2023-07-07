from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views.brands import BrandView
from .views.cars import CarDetail, CarList, CarRentView, RentedCarsView, RentCustomPrice  # CarsView,
from .views.categories import CategoryView
from .views.features import FeaturesView
from .views.reviews import ReviewDetail, ReviewList, ReviewsView

router = DefaultRouter()
router.register(r"cars", CarList, basename="cars")
router.register(r"reviews", ReviewList, basename="reviews")

urlpatterns = [
    path("", include(router.urls)),
    path("features/", FeaturesView.as_view(), name="features-list-create"),
    path("categories/", CategoryView.as_view(), name="category-list-create"),
    path("brands/", BrandView.as_view(), name="brand-list-create"),
    # path("reviews/", ReviewsView.as_view(), name="review-list-create"),
    # --------------------
    path("cars/<car_id>/rent/", CarRentView.as_view(), name="book-car"),
    path("rented-cars/", RentedCarsView.as_view(), name="booked-cars"),
    # -----------------------
    path('cars/<pk>/', CarDetail.as_view(), name='car-detail'),
    # ------------------------
    path(
        "cars/<pk>/reviews/",
        CarList.as_view({"get": "reviews", "post": "add_reviews"}),
        name="car-reviews",
    ),
    path("cars/<car_id>/reviews/<pk>/", ReviewDetail.as_view(), name="review-detail"),
    # -------------------------
    # path('cars/<pk>/features/', ReviewList.as_view(), name='review-list'),

    # ---------------
    # Route for calculating the price of a car depending on the duration
    path("cars/<car_id>/rent/price", RentCustomPrice.as_view(), name='rent_price')

]

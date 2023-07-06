from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# from .views import RegisterView, LoginView, TokenRefreshView, UserDetailsView
from .views import RegisterView, UserDetailsView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", TokenObtainPairView.as_view(), name="login"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token-refresh"),
    path("users/me/", UserDetailsView.as_view(), name="user-details"),
]

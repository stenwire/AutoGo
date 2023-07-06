from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "api/v1/",
        include(
            [
                path("auth/", include("authme.urls")),
                path("", include("cars.urls")),
            ]
        ),
    ),
]

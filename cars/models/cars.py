import uuid

from django.contrib.auth import get_user_model
from django.db import models
from django.urls.base import reverse

from utils.models import TrackObjectStateMixin

User = get_user_model()


class Cars(TrackObjectStateMixin):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(
        max_length=255, blank=False, unique=True, verbose_name="Name"
    )
    description = models.TextField(max_length=255, blank=False)
    price = models.DecimalField(blank=False, max_digits=1000000000000, decimal_places=2)
    brand = models.ForeignKey("Brand", on_delete=models.CASCADE)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    features = models.ManyToManyField("Features")
    pickup_time = models.DateTimeField()
    dropoff_time = models.DateTimeField()
    pickup_location = models.CharField(max_length=255, verbose_name="Pickup Location")
    dropoff_location = models.CharField(max_length=255, verbose_name="Dropoff Location")
    available = models.BooleanField(default=True, blank=True, null=True)
    booked_by = models.UUIDField(blank=True, null=True)

    OWNER_FIELD = "user"

    class Meta:
        ordering = ["-created"]

    def get_reviews(self):
        return self.reviews.all()

    def __str__(self):
        return f"{self.brand} {self.name}"

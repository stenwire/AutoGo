from django.contrib.auth import get_user_model
from django.db import models
from django.urls.base import reverse
from utils.models import TrackObjectStateMixin

User = get_user_model()

from .cars import Cars


class RentedCars(TrackObjectStateMixin):
    car = models.ForeignKey("Cars", on_delete=models.CASCADE)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)  # Add this line

    # OWNER_FIELD = "user"

    class Meta:
        ordering = ["-last_updated"]

    def __str__(self):
        return self.name

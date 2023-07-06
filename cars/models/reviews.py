from django.contrib.auth import get_user_model
from django.db import models
from django.urls.base import reverse
from utils.models import TrackObjectStateMixin

from .cars import Cars

User = get_user_model()


class Reviews(TrackObjectStateMixin):
    car = models.ForeignKey("Cars", on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    content = models.TextField()
    rating = models.DecimalField(max_digits=2, decimal_places=1)

    def __str__(self):
        return f"Review for {self.car} by {self.user}"

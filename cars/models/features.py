from django.db import models
from django.urls.base import reverse

from utils.models import TrackObjectStateMixin


class Features(TrackObjectStateMixin):
    name = models.CharField(max_length=255, unique=True, verbose_name="Name")

    def __str__(self):
        return self.name

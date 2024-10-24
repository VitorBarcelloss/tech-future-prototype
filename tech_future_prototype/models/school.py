from django.contrib.auth.models import AbstractUser
from django.db import models


class School(AbstractUser):
    name = models.CharField(max_length=128, blank=False, null=False)
    is_public = models.BooleanField(default=False)
    enabled = models.BooleanField(default=False)

    objects = models.Manager()

    def __str__(self):
        return self.name
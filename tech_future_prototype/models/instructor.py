from django.contrib.auth.models import AbstractUser
from django.db import models


class Instructor(AbstractUser):
    birth_date = models.DateField(null=False)
    skills = models.JSONField(null=False)
    reviews = models.JSONField(null=True, blank=True)
    volunteer = models.BooleanField(default=True)
    enabled = models.BooleanField(default=False)
    lecture = models.ForeignKey('Lecture', on_delete=models.SET_NULL, null=True, blank=True, related_name='instructors')
    course = models.ForeignKey('Course', on_delete=models.CASCADE, null=True, blank=True, related_name='instructors')

    def __str__(self):
        return self.get_full_name()
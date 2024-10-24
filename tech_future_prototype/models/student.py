from django.contrib.auth.models import AbstractUser
from django.db import models


class Student(AbstractUser):
    birth_date = models.DateField(null=True, blank=True)
    subscriptions = models.ManyToManyField('Course', related_name='students')
    lecture = models.ManyToManyField('Lecture', related_name='students')
    interest = models.JSONField(null=True, blank=True)



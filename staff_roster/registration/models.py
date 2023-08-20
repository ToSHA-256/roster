from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    name = models.CharField(max_length=30, blank=True)
    surname = models.CharField(max_length=30, blank=True)
    patronymic = models.CharField(max_length=30, blank=True)

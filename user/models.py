from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Custom user model"""
    status = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.username

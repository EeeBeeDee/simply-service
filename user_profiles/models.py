from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    phone = models.IntegerField()

    def __str__(self):
        return self.username

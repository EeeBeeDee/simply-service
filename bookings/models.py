from django.db import models
from django.contrib.auth.models import User
from simply_service import settings
from django import forms

# Create your models here.


class Bookings(models.Model):
    RESTAURANTS = [
        ('TS', 'Tonys'),
        ('ZT', 'Zaytoons'),
        ('MR', 'Mercedes'),
        ('AU', 'Audi'),
    ]
    restaurant = models.CharField(max_length=100, choices=RESTAURANTS)
    time = models.TimeField()
    date = models.DateField()
    no_of_adults = models.CharField(max_length=2)
    no_of_children = models.CharField(max_length=2)
    name = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    email = models.EmailField()
    number = models.CharField(max_length=20)
    slug = models.SlugField(max_length=200, unique=True)


    def __str__(self):
        return str(self.name)

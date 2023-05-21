from django.db import models
from user_profiles.models import UserProfile
from django import forms


class Bookings(models.Model):
    """
    DB Model for individual bookings.
    """
    RESTAURANTS = [
        ('Tonys', 'Tonys'),
        ('The Char Grill', 'The Char Grill'),
        ('Mama Mia', 'Mama mia'),

    ]
    restaurant = models.CharField(max_length=100, choices=RESTAURANTS)
    time = models.TimeField()
    date = models.DateField()
    no_of_adults = models.CharField(max_length=2)
    no_of_children = models.CharField(max_length=2)
    name = models.ForeignKey(UserProfile, default=None,
                             on_delete=models.CASCADE)
    email = models.EmailField()
    number = models.CharField(max_length=20)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return str(self.name)

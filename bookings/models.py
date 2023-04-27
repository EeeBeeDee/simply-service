from django.db import models

# Create your models here.


class Bookings(models.Model):
    restaurant = models.CharField(max_length=100)
    time = models.TimeField()
    date = models.DateField()
    no_of_adults = models.CharField(max_length=2)
    no_of_children = models.CharField(max_length=2)
    name = models.CharField(max_length=20)
    email = models.EmailField()
    number = models.CharField(max_length=20)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.name

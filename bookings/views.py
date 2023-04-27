from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Bookings


# Create your views here.


def bookings(request):
    """
    Bookings view
    """
    return render(request, 'bookings.html')


def your_bookings(request):
    bookings = Bookings.objects.all()
    return render(request, 'your_bookings.html', {'bookings': bookings})

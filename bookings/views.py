from django.shortcuts import render, get_object_or_404
from django.views import generic, View

# Create your views here.


def bookings(request):
    """
    Bookings view
    """
    return render(request, 'bookings.html')

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views import generic, View
from .models import Bookings
from .forms import BookingsForm

# Create your views here.


def bookings(request):
    """
    Bookings view
    """
    if request.method == "POST":
        form = BookingsForm(request.POST)
        if form.is_valid():
            pass

    
    form = BookingsForm()    
    return render(request, 'bookings.html', {'form': form })


def your_bookings(request):
    bookings = Bookings.objects.all()
    return render(request, 'your_bookings.html', {'bookings': bookings})


def booking_detail(request, slug):
    bookings = Bookings.objects.all()
    booking = get_object_or_404(bookings, slug=slug)

    return render(request, 'booking_detail.html', {'booking': booking})

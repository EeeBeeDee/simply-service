from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views import generic, View
from .models import Bookings
from .forms import BookingsForm

# Create your views here.


def bookings(request):
    """
    Make a reservation page
    """
    if request.method == "POST":
        form = BookingsForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.name = request.user
            instance.slug = f'{instance.name}-{instance.date}'
            instance.save()
            return redirect('/')
    else:
        form = BookingsForm()
    return render(request, 'bookings.html', {'form': form})


def your_bookings(request):
    bookings = Bookings.objects.all()
    return render(request, 'your_bookings.html', {'bookings': bookings})


def booking_detail(request, slug):
    bookings = Bookings.objects.all()
    booking = get_object_or_404(bookings, slug=slug)

    return render(request, 'booking_detail.html', {'booking': booking})

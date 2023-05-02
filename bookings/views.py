from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views import generic, View
from django.contrib import messages
from .models import Bookings
from .forms import BookingsForm

# Create your views here.

@login_required()
def bookings(request):
    """
    Make a reservation page
    """
    user = get_object_or_404(User, username=request.user)
    if request.method == "POST":
        form = BookingsForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.name = user
            instance.slug = f'{instance.name}-{instance.date}'
            instance.save()
            messages.success(
                    request, f'Your reservation at {instance.restaurant} has been confirmed.')
            return redirect('homepage')
        else:
             print(form.errors.as_data())
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

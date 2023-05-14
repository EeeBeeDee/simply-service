from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
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
            current_time = str(instance.time)
            current_time = current_time.replace(":", "")
            instance.slug = f'{instance.name}-{current_time}-{instance.date}'
            instance.save()
            messages.success(request, "Your reservation has been accepted!")
            return redirect('your_bookings')
        else:
            messages.error(request, ("Your reservation could not be made,"
            "please try again."))
    else:
        form = BookingsForm()
    return render(request, 'bookings.html', {'form': form})


class YourBookings(LoginRequiredMixin, View):
    
    def get(self, request):
        bookings = Bookings.objects.filter(name=request.user)
        # bookings = get_object_or_404(queryset)
        # print(bookings)
        return render(request, 'your_bookings.html', {'bookings': bookings})

    # bookings = Bookings.objects.filter()
    # return render(request, 'your_bookings.html', {'bookings': bookings})


@login_required()
def booking_detail(request, slug):
    bookings = Bookings.objects.filter()
    booking = get_object_or_404(bookings, slug=slug)

    if request.method == "POST":
        booking = get_object_or_404(Bookings, slug=slug)
        booking.delete()
        messages.success(request, "Your booking has been successfully cancelled")
        return HttpResponseRedirect(reverse('your_bookings'))

    return render(request, 'booking_detail.html', {'booking': booking})

@login_required()
def booking_update(request, id):
    booking = get_object_or_404(Bookings, id=id)
    form = BookingsForm(request.POST or None, instance=booking)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "Your booking has been successfully updated")
            return redirect(booking_detail, slug=booking.slug)
        else:
            messages.error(request, "There was an error. Please try again.")

    context = {
        "booking": booking,
        "form": form,
    }
    return render(request, "booking_update.html", context)

# @login_required()
# def booking_update(request, id):
#     booking = get_object_or_404(Bookings, id=id)
#     form = BookingsForm(request.POST or None, instance=booking)
#     if request.method == "POST":
#         if form.is_valid():
#             # instance = form.save(commit=False)
#             current_time = str(form.instance.time)
#             current_time = current_time.replace(":", "")
#             form.instance.slug = f'{form.instance.name}-{current_time}-{form.instance.date}'
#             form.save()
#             return redirect('your_bookings')

#     return render(request, 'booking_update.html',
#         {'booking': booking,
#         "form": form})

# initial={'email': request.user.email}
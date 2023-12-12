from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.views import View
from django.contrib import messages
from user_profiles.models import UserProfile
from .models import Bookings
from .forms import BookingsForm

# Create your views here.


@login_required()
def bookings(request):
    """
    Make a reservation page
    """
    user = get_object_or_404(UserProfile, username=request.user)
    form = BookingsForm()
    print(user.phone)
    if request.method == "POST":
        form = BookingsForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.name = user
            instance.email = user.email
            current_time = str(instance.time)
            current_time = current_time.replace(":", "")
            instance.slug = f'{instance.name}-{current_time}-{instance.date}'
            instance.save()
            messages.success(request, "Your reservation has been accepted!")
            if user.email:
                send_mail(
                    f"Dinner reservation in {instance.restaurant}",
                    (f"Hi {instance.name},\n\nYou "
                        f"are booked into {instance.restaurant} "
                        f"on the {instance.date} at {instance.time}. \n"
                        "If you need to cancel or update your booking please "
                        "use our website. \n\nBest regards, \n\n"
                        "Simply Service Team"),
                    "simplyservice.bookings@gmail.com",
                    [user.email]
                )
            return redirect('your_bookings')
        else:
            print(form.errors.as_data())
            print(user.email)
            messages.error(request, ("Your reservation could not be "
                                     "made, please try again."))
    else:
        form = BookingsForm(initial={'number': user.phone,
                                     'email': user.email})
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
        messages.success(request, ("Your booking has been "
                                   "successfully cancelled"))
        return HttpResponseRedirect(reverse('your_bookings'))

    return render(request, 'booking_detail.html', {'booking': booking})


@login_required()
def booking_update(request, id):
    booking = get_object_or_404(Bookings, id=id)
    form = BookingsForm(request.POST or None, instance=booking)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, ("Your booking has been "
                                       "successfully updated"))
            return redirect(booking_detail, slug=booking.slug)
        else:
            messages.error(request, "There was an error. Please try again.")

    context = {
        "booking": booking,
        "form": form,
    }
    return render(request, "booking_update.html", context)


def booking2(request):

    return render(request, "booking2.html")

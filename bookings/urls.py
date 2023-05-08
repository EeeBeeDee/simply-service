from django.urls import path
from . import views


urlpatterns = [
    path('', views.bookings, name='bookings'),
    path('your_bookings/', views.YourBookings.as_view(), name='your_bookings'),
    path('<slug:slug>/', views.booking_detail, name='booking_detail'),
    path('update/<int:id>/', views.booking_update, name='booking_update'),

]

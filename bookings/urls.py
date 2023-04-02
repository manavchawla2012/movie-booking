from django.urls import path

from bookings.views import BookingLCView

BookingUrls = [
    path('', BookingLCView.as_view(), name="booking"),
]
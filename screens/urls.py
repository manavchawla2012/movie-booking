from django.urls import path
from screens.views import MovieLCView, ScreenLCView, SeatLCView, ShowLCView, AvailableSeats

ScreenUrls = [
    path('movie/', MovieLCView.as_view(), name="movie_lc"),
    path('', ScreenLCView.as_view(), name="screen_lc"),
    path('<uuid:screen_id>/seat/', SeatLCView.as_view(), name="seat_lc"),
    path('show/', ShowLCView.as_view(), name="show_lc"),
    path('show/<uuid:show_id>/status', AvailableSeats.as_view(), name='show_status'),
]

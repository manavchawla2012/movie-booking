from django.db.models import Q
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework import exceptions

from screens.serializers import MovieSerializer, MovieModel, ScreenSerializer, ScreenModel, SeatSerializer, SeatModel, \
    ShowsSerializer, ShowsModel


# Create your views here.

class MovieLCView(ListCreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = MovieSerializer
    queryset = MovieModel.objects


class ScreenLCView(ListCreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ScreenSerializer
    queryset = ScreenModel.objects


class SeatLCView(ListCreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = SeatSerializer
    queryset = SeatModel.objects

    def get_screen(self) -> ScreenModel:
        screen_id = self.kwargs['screen_id']
        screen = ScreenModel.objects.filter(id=screen_id).first()
        if not screen:
            raise exceptions.NotFound("Invalid Screen Id")
        return screen

    def get_queryset(self):
        screen = self.get_screen()
        return super(SeatLCView, self).get_queryset().filter(screen=screen)

    def create(self, request, *args, **kwargs):
        screen = self.get_screen()
        request.data['screen'] = screen.id
        return super(SeatLCView, self).create(request, *args, **kwargs)


class ShowLCView(ListCreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ShowsSerializer
    queryset = ShowsModel.objects


class AvailableSeats(APIView):
    permission_classes = (AllowAny,)

    def get(self, *args, **kwargs):
        show_id = self.kwargs['show_id']
        show = ShowsModel.objects.filter(id=show_id).first()
        if not show:
            raise exceptions.NotFound('Invalid Show Id')
        from bookings.models import BookingModel
        booked_seat_ids = BookingModel.objects.filter(show_id=show_id,
                                                      status__in=BookingModel.success_booking_status()).values_list(
            'seat_id', flat=True)
        available_seats = show.screen.seatmodel_set.filter(~Q(id__in=booked_seat_ids))
        booked_seats = SeatModel.objects.filter(id__in=booked_seat_ids)
        return Response(
            {
                "available_seats": SeatSerializer(instance=available_seats, many=True).data,
                "booked_seats": SeatSerializer(instance=booked_seats, many=True).data
            }
        )

from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import AllowAny

from bookings.serializers import BookingModel, BookingSerializer


# Create your views here.


class BookingLCView(ListCreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = BookingSerializer
    queryset = BookingModel.objects.filter(status__in=BookingModel.success_booking_status())

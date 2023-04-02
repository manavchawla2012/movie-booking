from rest_framework import serializers, exceptions

from bookings.models import BookingModel
from screens.models import ShowsModel, SeatModel


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingModel
        fields = "__all__"
        write_only_fields = ('user_id', 'show_id', 'seat_id')

    def validate_seat_id_for_show(self, seat_id, show: ShowsModel):
        seat = SeatModel.objects.filter(id=seat_id, screen_id=show.screen_id).first()
        if not seat:
            raise serializers.ValidationError("Invalid Seat for show")
        return seat

    def validate_seat_availability(self, seat_id, show_id):
        booking = BookingModel.objects.filter(seat_id=seat_id, show_id=show_id,
                                              status__in=BookingModel.success_booking_status()).first()
        if booking:
            raise serializers.ValidationError("Seat Already Booked")
        return booking

    def validate(self, attrs):
        show = ShowsModel.objects.filter(id=attrs["show_id"]).first()
        if not show:
            raise serializers.ValidationError("Invalid Show")
        _ = self.validate_seat_id_for_show(attrs["seat_id"], show)
        _ = self.validate_seat_availability(attrs["seat_id"], show.id)
        return super(BookingSerializer, self).validate(attrs)

    def create(self, validated_data):
        return super(BookingSerializer, self).create(validated_data)

    def update(self, instance, validated_data):
        raise exceptions.APIException("Method Not allowed")

import uuid
from typing import List

from django.db import models
from bookings.apps import BookingsConfig as AppConfig


# Create your models here.


class BookingModel(models.Model):
    id = models.UUIDField(primary_key=True, null=False, blank=False, default=uuid.uuid4)
    show_id = models.UUIDField(null=False, blank=False)
    user_id = models.UUIDField(null=False, blank=False)
    # We can keep as array field in future so that user can make multiple bookings
    """ 
        Or we can create booking model and create another model where store booking id, show id and seat id where 
        seat id and show id can be unique
    """
    seat_id = models.UUIDField(null=False, blank=False)
    status = models.IntegerField(choices=((1, 'booked'), (2, 'cancelled'), (3, 'completed')), default=1)
    created_on = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    updated_on = models.DateTimeField(auto_now=True, null=False, blank=False)

    class Meta:
        managed = True
        db_table = str(AppConfig.name)
        unique_together = (('show_id', 'seat_id'),)

    @staticmethod
    def success_booking_status() -> List[int]:
        return [1, 3]

    @staticmethod
    def failed_booking_status() -> List[int]:
        return [2]

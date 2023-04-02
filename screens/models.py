import uuid

from django.db import models

from screens.apps import ScreensConfig as AppConfig


# Create your models here.


class ScreenModel(models.Model):
    id = models.UUIDField(primary_key=True, null=False, blank=False, default=uuid.uuid4)
    name = models.CharField(null=False, blank=False, unique=True, max_length=20)
    is_active = models.BooleanField(null=False, blank=False, default=True)
    created_on = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    updated_on = models.DateTimeField(auto_now=True, null=False, blank=False)

    class Meta:
        managed = True
        db_table = str(AppConfig.name)


class SeatModel(models.Model):
    id = models.UUIDField(primary_key=True, null=False, blank=False, default=uuid.uuid4)
    row = models.IntegerField(null=False, blank=False)
    column = models.CharField(null=False, blank=False, max_length=2)
    screen = models.ForeignKey(ScreenModel, on_delete=models.CASCADE, null=False, blank=False)
    created_on = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    updated_on = models.DateTimeField(auto_now=True, null=False, blank=False)

    class Meta:
        managed = True
        db_table = str(AppConfig.name) + '_seat'
        unique_together = (('screen', 'column', 'row'),)


class MovieModel(models.Model):
    id = models.UUIDField(primary_key=True, null=False, blank=False, default=uuid.uuid4)
    movie_name = models.CharField(null=False, blank=False, max_length=20)
    created_on = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    updated_on = models.DateTimeField(auto_now=True, null=False, blank=False)

    class Meta:
        managed = True
        db_table = str(AppConfig.name) + '_movie'


class ShowsModel(models.Model):
    id = models.UUIDField(primary_key=True, null=False, blank=False, default=uuid.uuid4)
    movie = models.ForeignKey(MovieModel, null=False, blank=False, on_delete=models.CASCADE)
    date = models.DateField(null=False, blank=False)
    start_time = models.TimeField(null=False, blank=False)
    end_time = models.TimeField(null=False, blank=False)
    screen = models.ForeignKey(ScreenModel, null=False, blank=False, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    updated_on = models.DateTimeField(auto_now=True, null=False, blank=False)

    class Meta:
        managed = True
        db_table = str(AppConfig.name) + '_shows'

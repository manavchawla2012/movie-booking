import datetime

from rest_framework import serializers
from rest_framework import exceptions
from django.utils.dateparse import parse_time

from screens.models import ScreenModel, SeatModel, MovieModel, ShowsModel


class ScreenSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScreenModel
        fields = "__all__"
        write_only_fields = ('name',)


class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeatModel
        fields = "__all__"
        write_only_fields = ('row', 'column', 'screen')


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieModel
        fields = "__all__"
        write_only_fields = ('movie_name',)


class ShowsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShowsModel
        fields = "__all__"
        write_only_fields = ('movie', 'start_time', 'end_time', 'screen')

    def validate_date(self, date):
        if date < datetime.date.today():
            raise serializers.ValidationError("Date should be greater than today")
        return date

    def validate_start_time(self, start_time):
        if start_time > parse_time(self.initial_data['end_time']):
            raise serializers.ValidationError("Start Time can't be less than end time")
        return start_time

    def check_for_overlapping_show(self, start_time, end_time, screen: ScreenModel):
        # todo write code to check overlapping date
        pass

    def validate(self, attrs):
        if not self.instance:
            self.check_for_overlapping_show(attrs['start_time'], attrs['end_time'], attrs['screen'])
        return super(ShowsSerializer, self).validate(attrs)

    def update(self, instance, validated_data):
        raise exceptions.APIException("Method Not allowed")

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from users.models import UserModel


def phone_no_validator(phone_no: str):
    return phone_no


class UserSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    phone_no = serializers.CharField(allow_null=False, allow_blank=False,
                                     validators=[phone_no_validator, UniqueValidator(queryset=UserModel.objects)])
    email_id = serializers.EmailField(allow_blank=False, allow_null=False,
                                      validators=[UniqueValidator(queryset=UserModel.objects)])

    class Meta:
        model = UserModel
        fields = ('name', 'email_id', 'phone_no', 'id')

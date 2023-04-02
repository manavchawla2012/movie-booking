import uuid

from django.db import models

from users.apps import UsersConfig as AppConfig


# Create your models here.


class UserModel(models.Model):
    id = models.UUIDField(primary_key=True, null=False, blank=False, default=uuid.uuid4)
    name = models.CharField(max_length=100, null=False, blank=False)
    email_id = models.EmailField(null=False, blank=False, unique=True)
    phone_no = models.CharField(null=False, blank=False, max_length=10, unique=True)

    created_on = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    updated_on = models.DateTimeField(auto_now=True, null=False, blank=False)

    class Meta:
        managed = True
        db_table = str(AppConfig.name)

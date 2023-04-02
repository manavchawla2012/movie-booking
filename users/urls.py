from django.urls import path

from users.views import UserLCView

UserUrls = [
    path("", UserLCView.as_view(), name="create_view"),
]

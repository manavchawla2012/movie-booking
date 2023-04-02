"""movieProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from bookings.urls import BookingUrls
from screens.urls import ScreenUrls
from users.urls import UserUrls

api_urls = [
    path("user/", include((UserUrls, 'users'), namespace='users')),
    path("screen/", include((ScreenUrls, 'screens'), namespace='screens')),
    path("booking/", include((BookingUrls, 'bookings'), namespace='bookings')),
]

urlpatterns = [
    path('api/', include((api_urls, 'movieProject'), namespace='movie'))
]

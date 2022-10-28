from urllib.parse import urlparse
from django.urls import path

from django.contrib import admin

from . import views

urlpatterns = [
    path('signup', views.signup, name = 'signup'),
    path('activate/<uidb64>/<token>',views.activate, name = 'activate'),
    path('signup', views.signup, name = 'signup'),
    path('signout', views.signout, name = 'signout'),
]

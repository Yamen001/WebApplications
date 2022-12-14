from django.urls import path
from django.contrib import admin

from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('signup', views.signup, name = 'signup'),
    path('activate/<uidb64>/<token>',views.activate, name = 'activate'),
    path('signout', views.signout, name = 'signout'),
]

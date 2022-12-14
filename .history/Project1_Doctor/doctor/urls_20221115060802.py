"""doctor URL Configuration

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
from django.urls import path
# the commented import is not supported in django 4.0
# from django.conf.urls import include,
from django.urls import re_path, include
from django.contrib import admin
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('main/', include('main.urls')),    
    # url(r'^$', views.index_redirect, name='index_redirect'),
    # url(r'^templates/', include('register.urls')),
    # url(r'^templates/', include('main.urls')),
    # url(r'^templates/', include('main.urls')),
    path('templates/', include('register,urls')),
    
    
]

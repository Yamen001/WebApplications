from django.urls import path


urlpatterns = [
    path('',views.user_login, name = "login")
]

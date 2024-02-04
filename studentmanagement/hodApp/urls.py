from django.urls import path
from . import views
urlpatterns = [
    path('home', views.hod_home, name="hod"),
    ]

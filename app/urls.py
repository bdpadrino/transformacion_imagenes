from django.contrib import admin
from django.urls import path, include

from .urls import *
from . import views

app_name = "app"

urlpatterns = [
    path('', views.principal, name="principal"),
    path('app/convert', views.principal, name="principal"),
]
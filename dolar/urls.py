from django import urls
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.cotizacion, name= 'dolar'),

]
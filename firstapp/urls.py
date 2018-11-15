from django.contrib import admin
from django.urls import path

from firstapp import views

urlpatterns = [
    path('main/', views.main),
    path('show/', views.show),
]

from django.contrib import admin
from django.urls import path,include
from arun import views


urlpatterns = [
   path('', views.home)
]
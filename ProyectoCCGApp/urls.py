from django.urls import path

from ProyectoCCGApp import views

urlpatterns = [
    path('', views.home, name="Home")

]

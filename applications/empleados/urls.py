from django.contrib import admin
from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('lista/', views.Inicio.as_view(), name = 'Pagina de Inicio')
]
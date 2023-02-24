from django.contrib import admin
from django.urls import path, re_path, include
from . import views

app_name = 'empleado_app'

urlpatterns = [
    path('index/', views.Inicio.as_view(), name = 'Pagina de Inicio'),

    path(
        "lista/",
        views.EmpleadosListView.as_view(),
        name="Lista de Empleados"
    ),
    path(
        'buscar/',
        views.BuscarEmpleadoListView.as_view(),
        name='Buscador de Empleados'
    ),
    path(
        'detalle/<pk>',
        views.EmpleadoDetailView.as_view(),
        name='Detalle del Empleado'
    ),
    path(
        "create/",
        views.EmpleadoCreateView.as_view(),
        name="Alta de Empleado"
    ),
    path(
        "update/<pk>",
        views.EmpleadoUpdateView.as_view(),
        name="Modificacion de Empleados"
    ),
    path(
        "delete/<pk>",
        views.EmpleadoDeleteView.as_view(),
        name="Eliminar Empleado"
    )
    
    
]
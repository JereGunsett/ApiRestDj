from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView
)
from .models import Empleado
from.forms import EmpleadoForm
from django.urls import reverse_lazy


class Inicio(TemplateView):
    template_name = 'index.html'


class EmpleadosListView(ListView):
    model = Empleado
    template_name = "empleados/lista.html"
    ordering = 'apellido'
    paginate_by = 20
    context_object_name = 'empleados'


class BuscarEmpleadoListView(ListView):
    model = Empleado
    template_name = "empleados/buscar.html"
    context_object_name = 'empleados'

    #Metodo para buscar por nombre y/o apellido
    def get_queryset(self):
        nombre = self.request.GET.get('nombre', '')
        apellido = self.request.GET.get('apellido', '')
        queryset = super().get_queryset()
        if nombre or apellido:
            queryset = queryset.filter(nombre__icontains=nombre, apellido__icontains=apellido)
        return queryset
    #Metodo de clases
    """def get_queryset(self):
        palabra_clave = self.request.GET.get('kword', '')
        lista = Empleado.objects.filter(
            apellido__icontains = palabra_clave
        )
        return lista"""


class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "empleados/detalle.html"
    context_object_name = 'detalle'


class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = "empleados/create.html"
    form_class = EmpleadoForm
    success_url = reverse_lazy("empleado_app:Lista de Empleados")

    def form_valid(self, form):
        emp = form.save(commit=False)
        emp.nombre_completo = emp.nombre + ' ' + emp.apellido
        emp.save()
        return super(EmpleadoCreateView, self).form_valid(form)
    

class EmpleadoUpdateView(UpdateView):
    model = Empleado
    template_name = "empleados/update.html"
    form_class = EmpleadoForm
    success_url = reverse_lazy("empleado_app:Lista de Empleados")

    def form_valid(self, form):
        emp = form.save(commit=False)
        emp.nombre_completo = emp.nombre + ' ' + emp.apellido
        emp.save()
        return super(EmpleadoUpdateView, self).form_valid(form)
    

class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "empleados/delete.html"
    success_url = reverse_lazy("empleado_app:Lista de Empleados")


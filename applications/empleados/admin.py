from django.contrib import admin
from .models import Empleado
# Register your models here.


class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        'apellido',
        'nombre',
        'area',
    )
    search_fields = ('apellido','nombre')
    list_filter = ('area',)

admin.site.register(Empleado, EmpleadoAdmin)
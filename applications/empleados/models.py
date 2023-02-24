from django.db import models
from applications.areas.models import Area

# Create your models here.
class Empleado(models.Model):

    nombre = models.CharField('Nombre', max_length=50)
    apellido = models.CharField('Apellido', max_length=50)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = ("Empleado")
        verbose_name_plural = ("Empleados")

    def __str__(self):
        return str(self.apellido + ' ' + self.nombre)

    #def get_absolute_url(self):
    #    return reverse("_detail", kwargs={"pk": self.pk})

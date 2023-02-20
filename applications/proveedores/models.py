from django.db import models
from django.core.validators import EmailValidator

# Create your models here.
class Proveedor(models.Model):

    nombre = models.CharField('Nombre del proveedor', max_length=50)
    telefono = models.CharField('Nro. de Telefono', max_length=50)
    email = models.EmailField(("Correo electronico"), max_length=254, validators=[EmailValidator()])


    class Meta:
        verbose_name = ("Proveedor")
        verbose_name_plural = ("Proveedores")

    def __str__(self):
        return self.nombre

    #def get_absolute_url(self):
    #    return reverse("Proveedor_detail", kwargs={"pk": self.pk})

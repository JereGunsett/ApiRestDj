from django.db import models
from applications.proveedores.models import Proveedor
from applications.categorias.models import Categoria

# Create your models here.
class Producto(models.Model):
    """Model definition for Producto."""

    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre del producto', max_length=50)
    descripcion = models.TextField(("Descripcion del producto"))
    cantidad = models.IntegerField(("Cantidad en stock"))
    precio = models.DecimalField(("Precio de compra del producto"), max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)

    class Meta:
        """Meta definition for Producto."""

        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return self.nombre
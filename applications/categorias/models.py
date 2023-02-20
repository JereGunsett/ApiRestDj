from django.db import models

# Create your models here.
class Categoria(models.Model):

    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre de la Categoria', max_length=50)

    class Meta:
        verbose_name = ("Categoria")
        verbose_name_plural = ("Categorias")

    def __str__(self):
        return self.nombre

    #def get_absolute_url(self):
    #    return reverse("Categoria_detail", kwargs={"pk": self.pk})

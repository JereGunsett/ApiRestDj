from django.db import models

# Create your models here.
class Area(models.Model):

    nombre = models.CharField('Nombre de el area', max_length=50)

    class Meta:
        verbose_name = ('Area')
        verbose_name_plural = ('Areas')

    def __str__(self):
        return self.nombre

    #def get_absolute_url(self):
    #    return reverse("Area_detail", kwargs={"pk": self.pk})

from django.db import models
from applications.areas.models import Area
from avatar_generator import Avatar

# Create your models here.
class Empleado(models.Model):

    nombre = models.CharField('Nombre', max_length=50)
    apellido = models.CharField('Apellido', max_length=50)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    avatar = models.ImageField('Avatar', upload_to='empleado', blank=True)
    
    # Generar como avatar las iniciales del usuario (NO FUNCIONO)
    # def save(self, *args, **kwargs):
    #     if not self.avatar: # Verifica que el avatar no exista ya
    #         avatar_generator = Avatar() # Crea una instancia de la clase Avatar
    #         image = avatar_generator.generate(self.apellido[0] + self.nombre[0]) # Genera el avatar con las iniciales del nombre y apellido
    #         self.avatar.save(f'{self.nombre}_{self.apellido}.png', image, save=False) # Guarda el avatar
    #     super().save(*args, **kwargs) # Llama al método save() del modelo padre

    class Meta:
        verbose_name = ("Empleado")
        verbose_name_plural = ("Empleados")

    def __str__(self):
        return str(self.apellido + ' ' + self.nombre)


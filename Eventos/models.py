from django.db import models

# Create your models here.
class Eventos(models.Model):
    nombre = models.CharField(max_length=100)
    fecha = models.DateField(null=True, blank=True)
    lugar = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre


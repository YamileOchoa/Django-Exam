from django.db import models
from autores.models import Autor

# Create your models here.
class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    fecha_created = models.DateTimeField(auto_now=True)
    genero = models.CharField(max_length=50)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

from django.db import models

# Create your models here.
class Permiso(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=80)
    descripcion = models.CharField(max_length=100)
    estado = models.BooleanField(default=True)

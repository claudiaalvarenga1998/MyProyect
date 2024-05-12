from django.db import models
from Aplicaciones.Usuario.models import Usuario

# Create your models here.

class Materia(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=80)
    descripcion = models.CharField(max_length=100)
    estado = models.BooleanField(default=True)


class MateriaProfesor(models.Model):
    id = models.AutoField(primary_key=True)
    id_materia = models.ForeignKey(Materia, null=False, on_delete=models.RESTRICT)
    id_profesor = models.ForeignKey(Usuario, null=False, on_delete=models.RESTRICT)

def _str_(self):
    return self.nombre  
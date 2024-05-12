from django.db import models

from Aplicaciones.Permiso.models import Permiso

# Create your models here.
class Rol(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=80)
    descripcion = models.CharField(max_length=100)
    estado = models.BooleanField(default=True)
    
class RolPermiso(models.Model):
    id = models.AutoField(primary_key=True)
    id_rol = models.ForeignKey(Rol, null=False, on_delete=models.RESTRICT)
    id_permiso = models.ForeignKey(Permiso, null=False, on_delete=models.RESTRICT)


def _str_(self):
    return  self.nombre
from django.db import models
from Aplicaciones.Persona.models import Persona
from Aplicaciones.Rol.models import Rol

# Create your models here.
class Usuario(models.Model):
    ci = models.OneToOneField(Persona, null=False, primary_key=True, on_delete=models.RESTRICT)
    password = models.CharField(max_length=50)
    fecha_alta = models.DateTimeField(auto_now_add=True)
    rol = models.ForeignKey(Rol, null=False, on_delete=models.RESTRICT)
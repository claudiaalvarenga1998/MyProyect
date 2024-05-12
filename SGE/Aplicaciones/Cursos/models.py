from django.db import models
from Aplicaciones.Persona.models import Persona
from Aplicaciones.Usuario.models import Usuario

class Curso(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=80)
    descripcion = models.CharField(max_length=100)
    estado = models.BooleanField(default=True)

class CursoMateriaProfesor(models.Model):
    id_curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    id_materia = models.ForeignKey('Materias.Materia', null=True, on_delete=models.CASCADE)
    id_profesor = models.ForeignKey('Usuario.Usuario', null=True,  on_delete=models.CASCADE)
    



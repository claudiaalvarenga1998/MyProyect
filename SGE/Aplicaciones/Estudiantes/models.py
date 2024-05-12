from django.db import models
from Aplicaciones.Persona.models import Persona
from Aplicaciones.Cursos.models import Curso

class Estudiante(models.Model):
    ci = models.OneToOneField(Persona, null=False, primary_key=True, on_delete=models.RESTRICT, default=1)
    curso = models.ForeignKey('Cursos.Curso', null=True, on_delete=models.SET_NULL)

def __str__(self):
        return str(self.ci)
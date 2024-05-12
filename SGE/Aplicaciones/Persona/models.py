from django.db import models

# Create your models here.
class Persona(models.Model):
    ci = models.PositiveIntegerField(primary_key=True, unique=True)
    nombres = models.CharField(max_length=80, null=False)
    apellidos = models.CharField(max_length=100,  null=False)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    direccion = models.CharField(max_length=500, null=False)
    telefono = models.CharField(max_length=20, null=False)
    email = models.CharField(max_length=50, null=False)
    sexos = [
        ('M', 'Masculino'),
        ('F', 'Femenino')
    ]
    sexo = models.CharField(max_length=1, choices = sexos, default ='F', null=False)
    estado = models.BooleanField(default=True)

def __str__(self):
        return self.ci
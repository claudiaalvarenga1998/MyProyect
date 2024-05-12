from django.db import models

class Institucion(models.Model):
    nombre = models.CharField(max_length=255)
    acronimo = models.CharField(max_length=20, blank=True)
    descripcion = models.TextField(blank=True)
    direccion = models.CharField(max_length=255, blank=True)
    ciudad = models.CharField(max_length=100, blank=True)
    departamento = models.CharField(max_length=100, blank=True)
    barrio = models.CharField(max_length=100, blank=True)
    pais = models.CharField(max_length=100, blank=True)
    sitio_web = models.URLField(blank=True)

    def __str__(self):
        return self.nombre
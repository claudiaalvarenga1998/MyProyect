from django.contrib  import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexEstudiantes, name = 'Estudiantes'),
    path('listar', views.listar, name = 'Listar'),
    path('agregar', views.agregar, name = 'Agregar'),
    path('actualizar', views.actualizar, name = 'Actualizar'),
    path('eliminar', views.eliminar, name = 'Eliminar'),
   
    
]
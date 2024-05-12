from django.contrib  import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexCursos, name = 'Cursos'),
    path('listar', views.listar, name = 'Listar'),
    path('agregar', views.agregar, name = 'Agregar'),
    path('actualizar', views.actualizar, name = 'Actualizar'),
    path('eliminar', views.eliminar, name = 'Eliminar'),
    path('buscar', views.buscar, name = 'Buscar')
    
]
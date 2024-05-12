from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from Aplicaciones.Persona.models import Persona
from Aplicaciones.Rol.models import Rol
from .models import Materia
# Create your views here.

TEMPLATE_DIRS = (
    'os.path.join(BASE_DIR, "templates")'
)

def indexMaterias(request):
   return  render(request,'gestionMaterias.html')

def listar(request):
    materias = Materia.objects.all()
    datos  = {'materias': materias}
    return  render(request,'crud_materias/listar.html', datos)

def agregar(request):
    if request.method == 'POST': # Si se ha enviado el formulario por POST...
        if request.POST['nombre'] and request.POST['descripcion'] and  request.POST['estado']:
            # Create a new Materia instance
            materia = Materia()
            materia.nombre = request.POST['nombre']
            materia.descripcion = request.POST['descripcion']
            materia.estado = request.POST['estado']
            materia.save()

            return redirect('Listar')
    else:
        return  render(request,'crud_materias/agregar.html')

def actualizar(request):
    if request.method == 'POST': # Si se ha enviado el formulario por POST...
        if request.POST['id'] and request.POST['nombre'] and request.POST['descripcion'] and  request.POST['estado']:
            # Create a new Materia instance
            materia = Materia()
            materia.id =  request.POST['id']
            materia.nombre = request.POST['nombre']
            materia.descripcion = request.POST['descripcion']
            materia.estado = request.POST['estado']
            materia.save()

            return redirect('Listar')
    else:
        materias = Materia.objects.all()
        datos  = {'materias': materias}
        return render(request,'crud_materias/actualizar.html', datos)

def eliminar(request):
    if request.method == 'POST': # Si se ha enviado el formulario por POST...
        if request.POST['id']:
            id_a_borrar =  int(request.POST['id'])
            tupla = Materia.objects.get(id=id_a_borrar)
            tupla.delete()
            return redirect('Listar')
    else:
        materias = Materia.objects.all()
        datos  = {'materias': materias}
        return  render(request,'crud_materias/eliminar.html', datos)
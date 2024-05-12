from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from Aplicaciones.Persona.models import Persona
from Aplicaciones.Rol.models import Rol
from .models import Curso
# Create your views here.

TEMPLATE_DIRS = (
    'os.path.join(BASE_DIR, "templates")'
)

def indexCursos(request):
   return  render(request,'gestionCursos.html')

def listar(request):
    cursos = Curso.objects.all()
    datos  = {'cursos': cursos}
    return  render(request,'crud_cursos/listar.html', datos)

def agregar(request):
    if request.method == 'POST': # Si se ha enviado el formulario por POST...
        if request.POST['nombre'] and request.POST['descripcion'] and  request.POST['estado']:
            # Create a new Curso instance
            curso = Curso()
            curso.nombre = request.POST['nombre']
            curso.descripcion = request.POST['descripcion']
            curso.estado = request.POST['estado']
            curso.save()

            return redirect('Listar')
    else:
        return  render(request,'crud_cursos/agregar.html')

def actualizar(request):
    if request.method == 'POST': # Si se ha enviado el formulario por POST...
        if request.POST['id'] and request.POST['nombre'] and request.POST['descripcion'] and  request.POST['estado']:
            # Create a new Curso instance
            curso = Curso()
            curso.id =  request.POST['id']
            curso.nombre = request.POST['nombre']
            curso.descripcion = request.POST['descripcion']
            curso.estado = request.POST['estado']
            curso.save()

            return redirect('Listar')
    else:
        cursos = Curso.objects.all()
        datos  = {'cursos': cursos}
        return  render(request,'crud_cursos/actualizar.html', datos)

def eliminar(request):
    if request.method == 'POST': # Si se ha enviado el formulario por POST...
        if 'id' in request.POST:
            id_a_borrar =  int(request.POST['id'])
            tupla = Curso.objects.get(id=id_a_borrar)
            tupla.delete()
            return redirect('Listar')
    else:
        cursos = Curso.objects.all()
        datos  = {'cursos': cursos}
        return  render(request,'crud_cursos/eliminar.html', datos)

def buscar(request):
    if request.method == 'GET':
        id = request.GET.get('id')
        if id:
            search_result = get_object_or_404(Curso, id=id)
            return render(request, 'crud_cursos/eliminar.html', {'search_result': search_result})
    return redirect('eliminar')
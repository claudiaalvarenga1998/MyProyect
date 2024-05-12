from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from Aplicaciones.Persona.models import Persona
from Aplicaciones.Cursos.models import Curso
from .models import Estudiante
# Create your views here.

TEMPLATE_DIRS = (
    'os.path.join(BASE_DIR, "templates")'
)

def indexEstudiantes(request):
   return  render(request,'gestionEstudiantes.html')

def listar(request):
    users = Estudiante.objects.all()
    datos  = {'estudiantes':users}
    return  render(request,'crud_estudiantes/listar.html', datos)

def agregar(request):
    if request.method == 'POST':  # Si se ha enviado el formulario por POST...
        if request.POST['ci'] and request.POST['nombres'] and request.POST['apellidos'] and request.POST['email'] and request.POST['telefono'] and request.POST['fecha_nac'] and request.POST['direccion'] and request.POST['sexo'] and request.POST['estado'] and request.POST['curso']:
            # Create a new Persona instance
            persona = Persona()
            persona.ci = int(request.POST['ci'])
            persona.nombres = request.POST['nombres']
            persona.apellidos = request.POST['apellidos']
            persona.email = request.POST['email']
            persona.telefono = request.POST['telefono']
            persona.fecha_nacimiento = request.POST['fecha_nac']
            persona.direccion = request.POST['direccion']
            persona.sexo = request.POST['sexo']
            persona.estado = request.POST['estado']
            persona.save()

            # Create a new Estudiante instance
            estudiante = Estudiante()
            estudiante.ci = persona
            estudiante.curso = Curso.objects.get(id=request.POST['curso'])
            estudiante.save()
            return redirect('Listar')
    else:
        # Retrieve all available course data
        cursos = Curso.objects.all()
        return render(request, 'crud_estudiantes/agregar.html', {'cursos': cursos})


def actualizar(request):
    if request.method == 'POST':
        ci = request.POST['ci']
        persona = Persona.objects.get(ci=ci)
        estudiante = Estudiante.objects.get(ci=persona)
        persona.nombres = request.POST['nombres']
        persona.apellidos = request.POST['apellidos']
        persona.email = request.POST['email']
        persona.telefono = request.POST['telefono']
        persona.fecha_nacimiento = request.POST['fecha_nac']
        persona.direccion = request.POST['direccion']
        persona.sexo = request.POST['sexo']
        persona.estado = request.POST['estado']
        persona.save()
        estudiante.curso = Curso.objects.get(id=request.POST['curso'])
        estudiante.save()
        return redirect('Listar')
    else:
        estudiantes = Estudiante.objects.all()
        cursos = Curso.objects.all()
        return render(request, 'crud_estudiantes/actualizar.html', {'estudiantes': estudiantes, 'cursos': cursos})

def eliminar(request):
    if request.method == 'POST': # Si se ha enviado el formulario por POST...
        if request.POST['ci']:
            ci_a_borrar =  int(request.POST['ci'])
            tupla = Estudiante.objects.get(ci=ci_a_borrar)
            tupla.delete()
            return redirect('Listar')
    else:
        users = Estudiante.objects.all()
        datos  = {'estudiantes':users}
        return  render(request,'crud_estudiantes/eliminar.html', datos)
    



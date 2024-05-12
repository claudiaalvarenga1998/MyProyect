from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from Aplicaciones.Persona.models import Persona
from Aplicaciones.Rol.models import Rol
from .models import Usuario 
# Create your views here.

TEMPLATE_DIRS = (
    'os.path.join(BASE_DIR, "templates")'
)

def indexUsuarios(request):
   return  render(request,'gestionUsuarios.html')

def listar(request):
    users = Usuario.objects.all()
    datos  = {'usuarios':users}
    return  render(request,'crud_usuarios/listar.html', datos)

def agregar(request):
    if request.method == 'POST': # Si se ha enviado el formulario por POST...
        if request.POST['ci']and  request.POST['nombres'] and request.POST['apellidos'] and  request.POST['email'] and  request.POST['telefono']  and request.POST['fecha_nac'] and request.POST['direccion'] and request.POST['sexo'] and request.POST['estado'] and request.POST['password'] and  request.POST['rol']:   
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

            # Create a new Usuario instance
            user = Usuario()
            user.ci = persona
            user.password = request.POST['password']
            user.fecha_alta = datetime.now()

            # Create a new Rol instance
            rol = Rol()
            rol.save()
            user.rol = rol
            user.save()
            return redirect('Listar')
    else:
        return  render(request,'crud_usuarios/agregar.html')

def actualizar(request):
    if request.method == 'POST': # Si se ha enviado el formulario por POST...
        if request.POST['ci'] and  request.POST['nombres'] and request.POST['apellidos'] and  request.POST['email'] and  request.POST['telefono']  and request.POST['fecha_nac'] and request.POST['direccion'] and request.POST['sexo'] and request.POST['estado'] and  request.POST['rol']:   
            
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

            # Create a new Usuario instance
            user = Usuario()
            user.ci = persona
            user.fecha_alta = datetime.now()

            # Create a new Rol instance
            rol = Rol()
            rol.save()
            user.rol = rol
            user.save()
            return redirect('Listar')
    else:
        users = Usuario.objects.all()
        datos  = {'usuarios':users}
        return  render(request,'crud_usuarios/actualizar.html', datos)

def eliminar(request):
    if request.method == 'POST': # Si se ha enviado el formulario por POST...
        if request.POST['ci']:
            ci_a_borrar =  int(request.POST['ci'])
            tupla = Usuario.objects.get(ci=ci_a_borrar)
            tupla.delete()
            return redirect('Listar')
    else:
        users = Usuario.objects.all()
        datos  = {'usuarios':users}
        return  render(request,'crud_usuarios/eliminar.html', datos)
    



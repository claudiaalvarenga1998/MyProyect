from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from Aplicaciones.Rol.models import Rol
from Aplicaciones.Usuario.models import Usuario
from Aplicaciones.Permiso.models import Permiso

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'Accounts/templates/login.html', {'error': 'Correo electrónico o contraseña no válidos'})
    else:
        return render(request, 'Accounts/templates/login.html')

def register_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        rol_id = request.POST['rol']
        rol = Rol.objects.get(id=rol_id)
        user = User.objects.create_user(email, email, password, rol=rol)
        login(request, user)
        return redirect('home')
    else:
        rol = Rol.objects.all()
        return render(request, 'Accounts/register.html', {'roles': roles})

@login_required
def permission_view(request):
    user = request.user
    permissions = Permission.objects.filter(rol=user.rol)
    return render(request, 'accounts/permissions.html', {'permissions': permissions})

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')
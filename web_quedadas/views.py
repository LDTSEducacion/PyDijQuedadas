# web_quedadas/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Quedada
from django.contrib import messages

def vista_principal(request):
    return render(request, 'vista_principal.html')

@login_required
def listar_quedadas(request):
    quedadas = Quedada.objects.all()
    return render(request, 'listar_quedadas.html', {'quedadas': quedadas})

@login_required
def crear_quedada(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        fecha = request.POST['fecha']
        creador = request.user
        quedada = Quedada.objects.create(nombre=nombre, fecha=fecha, creador=creador)
        quedada.participantes.add(creador)
        messages.success(request, 'Quedada creada exitosamente.')
        return redirect('listar_quedadas')
    return render(request, 'crear_quedada.html')



@login_required
def listar_usuarios(request):
    usuarios = User.objects.all()
    return render(request, 'listar_usuarios.html', {'usuarios': usuarios})

@login_required
def crear_usuario(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            messages.success(request, f'Usuario {username} creado exitosamente.')
            return redirect('listar_usuarios')
        except Exception as e:
            messages.error(request, f'Error al crear usuario: {e}')
    return render(request, 'crear_usuario.html')

def eliminar_usuario(request, user_id):
    if request.method == 'POST':
        try:
            user = User.objects.get(id=user_id)
            user.delete()
            messages.success(request, 'Usuario eliminado exitosamente.')
        except User.DoesNotExist:
            messages.error(request, 'Usuario no encontrado.')
    return redirect('listar_usuarios')

def eliminar_quedada(request, quedada_id):
    if request.method == 'POST':
        try:
            quedada = Quedada.objects.get(id=quedada_id)
            quedada.delete()
            messages.success(request, 'Quedada eliminada exitosamente.')
        except Quedada.DoesNotExist:
            messages.error(request, 'Quedada no encontrada.')
    return redirect('listar_quedadas')


# Atajos de Django (validación y carga de html, y demás)
from django.shortcuts import render, redirect, get_object_or_404
# Autenticación y login
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Manejo de mensajes de alerta e informe con Django
from django.contrib import messages
# Importación de los modelos necesarios en esta página
from usuarios.models import Persona, Usuario, UsuarioManager
# Formularios necesarios en esta página
from .forms import RegistroUsuarioForm, EditarUsuarioForm
from typing import cast


# Login de usuarios
def login_usuario(request):
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        clave = request.POST.get('clave')
        usuario_auth = authenticate(request, username=usuario, password=clave)
        if usuario_auth is not None:
            login(request, usuario_auth)
            return redirect('inicio')  # El nombre debe ser adaptado
        else:
            messages.error(request, 'Credenciales inválidas')
    return render(request, 'login.html')


# logout
@login_required
def logout_usuario(request):
    logout(request)
    return redirect('login')


@login_required
def inicio(request):
    return render(request, 'inicio.html')


# Creaación de usuarios
def registro_usuario(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)

        if form.is_valid():
            # Primero, creamos la persona (esto ya lo haces)
            persona = Persona.objects.create(
                nombre=form.cleaned_data['nombre'],
                apellidos=form.cleaned_data['apellidos'],
                tipo_iden=form.cleaned_data['tipo_iden'],
                num_iden=form.cleaned_data['num_iden'],
                correo=form.cleaned_data['correo'],
                tel=form.cleaned_data['tel']
            )

            # Luego, creamos el usuario forzando el tipo del manager
            usuario = cast(UsuarioManager, Usuario.objects).create_user(
                usuario=form.cleaned_data['usuario'],
                clave=form.cleaned_data['clave'],
                rol=form.cleaned_data['rol'],
                foto=form.cleaned_data['foto'],
                id_persona=persona
            )

            # Aquí puedes redirigir o hacer lo que necesites
            return redirect('login')  # o alguna otra vista

    else:
        form = RegistroUsuarioForm()

    return render(request, 'registro_usuario.html', {'form': form})


# Lectura de Usuarios
# Listado de usuarios
@login_required
def lista_usuarios(request):
    usuarios = Usuario.objects.select_related('id_persona').all()
    return render(request, 'lista_usuarios.html', {'usuarios': usuarios})

# Detalles de usuario
@login_required
def detalle_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    return render(request, 'detalle_usuario.html', {'usuario': usuario})


# Editar usuario
@login_required
def editar_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == 'POST':
        form = EditarUsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario actualizado correctamente.')
            return redirect('detalle_usuario', pk=usuario.pk)
    else:
        form = EditarUsuarioForm(instance=usuario)
    return render(request, 'editar_usuario.html', {'form': form})


# Eliminar usuario
@login_required
def eliminar_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == 'POST':
        usuario.delete()
        messages.success(request, 'Usuario eliminado correctamente.')
        return redirect('lista_usuarios')
    return render(request, 'eliminar_usuario.html', {'usuario': usuario})
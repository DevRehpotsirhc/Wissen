# Atajos de Django (validación y carga de html, y demás)
from django.shortcuts import render, redirect, get_object_or_404
# Autenticación y login
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
# Manejo de mensajes de alerta e informe con Django
from django.contrib import messages
# Importación de los modelos necesarios en esta página
from usuarios.models import Administrador, Docente, Estudiante, Persona, Usuario, Materia, Curso
# Integridad de los datos
from django.db import transaction
# Formularios necesarios en esta página
from .forms import EditarUsuarioForm
# Otras importaciones necesarias
from datetime import datetime




# Variables globales
def globals(request):
    return {'fecha': datetime.now().year}


# Login de usuarios
def login_usuario(request):
    if request.user.is_authenticated:
        return redirect('inicio')
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        clave = request.POST.get('clave')
        usuario_auth = authenticate(request, username=usuario, password=clave)
        if usuario_auth is not None:
            login(request, usuario_auth)
            return redirect('inicio')
        else:
            messages.error(request, 'Credenciales inválidas')
    return render(request, 'login.html')


# Logout del sistema
@login_required
def logout_usuario(request):
    logout(request)
    return redirect('login')


# Página de inicio del sistema
@login_required
def inicio(request):
    return render(request, 'inicio.html')


def user_admin(user):
    return user.is_authenticated and user.rol == 'admin'
# Creación de usuario
@user_passes_test(user_admin, login_url='login')
def registro_usuario(request):
    if request.method == 'POST':
        try:
            with transaction.atomic():
                # Recolección de los datos del formulario
                nombre = request.POST.get('nombre')
                apellidos = request.POST.get('apellidos')
                tipo_iden = request.POST.get('tipo_iden')
                num_iden = request.POST.get('num_iden')
                correo = request.POST.get('correo')
                tel = request.POST.get('tel')
                usuario_txt = request.POST.get('usuario')
                clave = request.POST.get('clave')
                rol = request.POST.get('rol')
                foto = request.POST.get('foto', '')

                # Creación de la persona
                persona = Persona.objects.create(
                    nombre=nombre,
                    apellidos=apellidos,
                    tipo_iden=tipo_iden,
                    num_iden=num_iden,
                    correo=correo,
                    tel=tel,
                )

                # Creación del usuario
                usuario = Usuario.objects.create_user(
                    usuario=usuario_txt,
                    clave=clave,
                    rol=rol,
                    foto=foto,
                    id_persona=persona,
                )

                # Roles
                if rol == 'admin':
                    cargo = request.POST.get('cargo')
                    Administrador.objects.create(id_usuario=usuario, cargo=cargo)

                if rol == 'docen':
                    materias_ids = request.POST.getlist('materias')
                    cursos_ids = request.POST.getlist('cursos')
                    docente = Docente.objects.create(id_usuario=usuario)
                    if docente:
                        docente.id_materia.set(materias_ids)
                        docente.id_curso.set(cursos_ids)
                    else:
                        raise ValueError("Debe seleccionar al menos una materia y un curso para el docente.")

                if rol == 'estud':
                    id_curso = request.POST.get('id_curso')
                    if id_curso:
                        curso = Curso.objects.get(id_curso=id_curso)
                        Estudiante.objects.create(id_usuario=usuario, id_curso=curso)
                    else:
                        raise ValueError("Curso requerido para estudiante.")

                messages.success(request, 'Usuario creado correctamente.')
                return redirect('lista_usuarios')

        except Exception as e:
            messages.error(request, f'Error en el registro: {str(e)}')

    materias = Materia.objects.all()
    cursos = Curso.objects.all()
    
    return render(request, 'registro_usuario.html', {'materias': materias, 'cursos': cursos})





#      ** CAMBIAR ESTAS VISTAS PARA ACTUAR SOBRE EL OBJETO DE PERSONA TAMBIÉN **




# Lectura de Usuarios
# Listado de usuarios
@user_passes_test(user_admin, login_url='login')
def lista_usuarios(request):
    usuarios = Usuario.objects.select_related('id_persona').all()
    return render(request, 'lista_usuarios.html', {'usuarios': usuarios})


# Detalles de usuario
@user_passes_test(user_admin, login_url='login')
def detalle_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    cargo = None
    materias = []
    cursos = []
    curso = None

    if usuario.rol == 'admin':
        admin = Administrador.objects.filter(id_usuario=usuario).first()
        cargo = admin.get_cargo_display() if admin else None # type: ignore
    elif usuario.rol == 'docen':
        docente = Docente.objects.filter(id_usuario=usuario).first()
        if docente:
            materias = [m.materia for m in docente.id_materia.all()]
            cursos = [c.curso for c in docente.id_curso.all()]
    elif usuario.rol == 'estud':
        estudiante = Estudiante.objects.filter(id_usuario=usuario).first()
        curso = estudiante.id_curso.curso if estudiante else None

    return render(request, 'detalle_usuario.html', {
        'usuario': usuario, 
        'cargo': cargo, 
        'materias': materias, 
        'cursos': cursos, 
        'curso': curso})


# Editar usuario
@user_passes_test(user_admin, login_url='login')
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
@user_passes_test(user_admin, login_url='login')
def eliminar_usuario(request, pk):
    usuario = get_object_or_404(Persona, pk=pk)
    if request.method == 'POST':
        usuario.delete()
        messages.success(request, 'Usuario eliminado correctamente.')
        return redirect('lista_usuarios')
    return render(request, 'eliminar_usuario.html', {'usuario': usuario})
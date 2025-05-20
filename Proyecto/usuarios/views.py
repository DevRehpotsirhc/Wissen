from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from .models import Persona, Usuario, Administrador, Docente, Estudiante
from .forms import RegistroUsuarioForm
from django.db import transaction, IntegrityError

def registro_usuario(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    persona = Persona.objects.create(
                        nombre=form.cleaned_data['nombre'],
                        apellidos=form.cleaned_data['apellidos'],
                        tipo_iden=form.cleaned_data['tipo_iden'],
                        num_iden=form.cleaned_data['num_iden'],
                        correo=form.cleaned_data['correo'],
                        tel=form.cleaned_data['tel']
                    )

                    usuario = Usuario.objects.create(
                        usuario=form.cleaned_data['usuario'],
                        clave=make_password(form.cleaned_data['clave']),
                        rol=form.cleaned_data['rol'],
                        foto=form.cleaned_data.get('foto'),
                        id_persona=persona
                    )

                    if usuario.rol == 'admin':
                        Administrador.objects.create(
                            id_usuario=usuario,
                            cargo=form.cleaned_data.get('cargo', 'adm')
                        )
                    elif usuario.rol == 'docen':
                        docente = Docente.objects.create(id_usuario=usuario)
                        docente.id_materia.set(form.cleaned_data['materias'])
                        docente.id_curso.set(form.cleaned_data['cursos'])
                    elif usuario.rol == 'estud':
                        Estudiante.objects.create(
                            id_usuario=usuario,
                            id_curso=form.cleaned_data['id_curso']
                        )

                    messages.success(request, 'Usuario registrado correctamente.')
                    return redirect('registro_usuario')
            except IntegrityError:
                form.add_error(None, "Error al registrar. Verifica los datos o intenta de nuevo.")
        else:
            messages.error(request, 'Corrige los errores del formulario.')
    else:
        form = RegistroUsuarioForm()

    return render(request, 'registro_usuario.html', {'form': form})
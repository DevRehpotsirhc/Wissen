from django import forms
from .models import Curso, Materia

class RegistroUsuarioForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellidos = forms.CharField(max_length=50)
    tipo_iden = forms.ChoiceField(choices=[
        ('ti', 'Tarjeta de Identidad'),
        ('ci', 'Cédula de Identidad'),
        ('ce', 'Cédula de Extrajería'),
        ('ppt', 'Permiso por Protección Temporal'),
    ])
    num_iden = forms.CharField(max_length=12)
    correo = forms.EmailField()
    tel = forms.CharField(max_length=15)

    usuario = forms.CharField(max_length=50)
    clave = forms.CharField(widget=forms.PasswordInput)
    rol = forms.ChoiceField(choices=[
        ('admin', 'Administrador'),
        ('docen', 'Docente'),
        ('estud', 'Estudiante'),
    ])
    foto = forms.CharField(max_length=250, required=False)
    
    cargo = forms.ChoiceField(
        choices=[('rec', 'Rector'), ('dir', 'Director'), ('adm', 'Administrador')],
        required=False
    )
    id_curso = forms.ModelChoiceField(queryset=Curso.objects.all(), required=False)
    materias = forms.ModelMultipleChoiceField(queryset=Materia.objects.all(), required=False)
    cursos = forms.ModelMultipleChoiceField(queryset=Curso.objects.all(), required=False)

from django import forms
from .models import Usuario


class EditarUsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['usuario', 'rol', 'estado', 'foto']
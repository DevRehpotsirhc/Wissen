from django import forms
from .models import Persona

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = [
            'nombre',
            'apellidos',
            'tipo_iden',
            'num_iden',
            'correo',
            'tel',
        ]
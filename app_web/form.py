from django import forms
from django.db import models
from django.contrib.auth.models import User
from .models import Perfil, Publicacion


class PublicacionForm(forms.ModelForm):
    class Meta:
        model = Publicacion
        fields = ['titulo', 'subtitulo', 'contenido', 'imagen_portada']
        
    def clean(self):
        cleaned_data = super().clean()
        titulo = cleaned_data.get('titulo')
        contenido = cleaned_data.get('contenido')
        if titulo and contenido:
            if len(titulo) > 20 and len(contenido) < 100:
                raise forms.ValidationError("Si el título es muy largo, el contenido debe ser más extenso.") #Error no asociado a un campo
        return cleaned_data


class EditarPerfil(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['foto']

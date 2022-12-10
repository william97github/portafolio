from django import forms
from .models import portafolio

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class portafolioforms(forms.ModelForm):
    class Meta:
        model = portafolio
        fields = ['autor', 'foto', 'titulo', 'descripcion', 'etiqueta', 'url']
        labels = {
            'autor': 'autor',
            'foto': 'Fotogracia',
            'titulo': 'Titulo de portafolio',
            'descripcion': 'Descripción',
            'etiqueta': 'Etiquetas utilizadas',
            'url': 'Url GitHub',
        }
        widgets = {
            'autor': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'ingrese una fotografia',
                    'id': 'autor',
                    'type': 'hidden',
                }
            ),
            'foto': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'ingrese una fotografia',
                    'id': 'foto',
                }
            ),
            'titulo': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'ingrese el titulo de portada',
                    'id': 'titulo',
                }
            ),
            'descripcion': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'ingrese la descripcion de portada',
                    'id': 'descripcion',
                    'rows': '3',
                }
            ),
            'etiqueta': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'ingrese una etiqueta',
                    'id': 'etiqueta',
                }
            ),
            'url': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'ingrese una url',
                    'id': 'url',
                }
            )
        }

class registrofroms(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Enter a valid email address')
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
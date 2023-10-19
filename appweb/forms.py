from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


class RegistroFormulario(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        

class ComentarioFormulario(forms.Form):

    tipo=forms.CharField(max_length=40)
    calificacion=forms.FloatField()
    opinion=forms.CharField(widget=forms.Textarea)


class ProductoFormulario(forms.ModelForm):
    
    class Meta:
        
        model = Producto
        
        fields = '__all__'
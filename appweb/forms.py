from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Avatar

class UserRegisterForm(UserCreationForm):
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


class ProductoFormulario(forms.Form):
    nombre = forms.CharField(max_length=100)
    descripcion = forms.CharField(widget=forms.Textarea)
    precio = forms.DecimalField(max_digits=10, decimal_places=2)
    stock = stock = forms.IntegerField(min_value=0)
    imagen = forms.ImageField(required=False)
    
class AvatarFormulario(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = '__all__'
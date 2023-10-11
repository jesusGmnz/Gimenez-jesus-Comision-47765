#from collections import User
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    rut=models.IntegerField()
    direccion=models.CharField(max_length=40)
    email=models.EmailField()
    
class Vendedor(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    numero_vendedor = models.CharField(max_length=20, unique=True)
    
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)
    
class Comentario(models.Model):
    producto = models.ForeignKey('Producto', on_delete=models.CASCADE)
    #usuario = models.ForeignKey(UserList, on_delete=models.CASCADE, related_name='comentarios')
    #contenido = models.TextField()
    #fecha_publicacion = models.DateTimeField(auto_now_add=True)
    
class Avatar(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)

    def __str__(self):
        return f"{self.user} - {self.imagen}"
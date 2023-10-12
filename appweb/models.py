#from collections import User
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
    
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    imagen = models.ImageField(upload_to='producto', null=True)
    
class Comentario(models.Model):
    autor=models.CharField(max_length=40, default="")
    tipo=models.CharField(max_length=40)
    calificacion=models.FloatField()
    opinion=models.TextField(max_length=300)
    
class Avatar(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)

    def __str__(self):
        return f"{self.user} - {self.imagen}"
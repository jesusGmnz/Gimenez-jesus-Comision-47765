from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from .models import *
from .forms import *

# Create your views here.
@login_required
def inicio(request):
    return render(request, "appweb/inicio.html")

def producto(request):
    
    todos = Producto.objects.all()

    return render(request, "appweb/producto.html",{"producto": todos})

def comentario(request):
    return render(request, "appweb/comentario.html")

def registroProducto(request):
    
    if request.method == "POST":
        
        miFormulario = ProductoFormulario(request.POST)
        
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            ProductoNuevo = Producto(nombre=informacion["nombre"], descripcion=informacion["descripcion"],precio=informacion["precio"],stock=informacion["stock"],imagen=informacion["imagen"],)
            ProductoNuevo.save()
            return render(request, "appweb/inicio.html")
    else:
        miFormulario = ProductoFormulario()
        
    return render(request, "appweb/registro_producto.html", {"form": miFormulario})

@login_required
def buscarProducto(request):

    return render(request, "appweb/buscar_producto.html")

@login_required
def resultadoProducto(request):

    if request.GET["nombre"]:

        nombre = request.GET["nombre"]
        Productoresultado = Producto.objects.filter(nombre__icontains=nombre)

        return render(request, "appweb/resultado_producto.html", {"bus":nombre, "res": Productoresultado})
    else:
        resultado = "No hay datos"

    return render(request, "appweb/resultado_producto.html", {resultado})

def eliminarProducto(request, producto_id):
    productoEliminado =Producto.objects.get(id= producto_id)
    productoEliminado.delete()
    todos =Producto.objects.all()

    return render(request, "appweb/producto.html", {"Producto": todos})

@login_required
def actualizarProducto(request,producto_nombre):
    
    ProductoElegido =Producto.objects.get(nombre=producto_nombre)
    
    if request.method == "POST":
        
        miFormulario = ProductoFormulario(request.POST)
        
        if miFormulario.is_valid():
            
            informacion = miFormulario.cleaned_data
            
            ProductoElegido.nombre = informacion["nombre"]
            ProductoElegido.descripcion = informacion["descripcion"]
            ProductoElegido.precio = informacion["precio"]
            ProductoElegido.stock = informacion["stock"]
            ProductoElegido.imagen = informacion["imagen"]
            
            ProductoElegido.save()
            
            return render(request, "appweb/inicio.html")
    else:
        miFormulario = ProductoFormulario(initial={"nombre": ProductoElegido.nombre,
                                                "descripcion": ProductoElegido.descripcion,
                                                "precio": ProductoElegido.precio,
                                                "stock": ProductoElegido.stock,
                                                "imagen": ProductoElegido.imagen})
        
    return render(request, "appweb/registro_producto.html", {"form": miFormulario})

@login_required
def agregarComentario(request):

    if request.method == 'POST':

        miFormulario=ComentarioFormulario(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            comentario = Comentario(autor=request.user,tipo=informacion['tipo'], calificacion=informacion['calificacion'], opinion=informacion["opinion"])

            comentario.save()

            return render(request, 'appweb/inicio.html')
    else:

        miFormulario=ComentarioFormulario()

    return render(request, 'appweb/añadir_comentario.html', {'form':miFormulario})

@login_required
def login_view(request):

    if request.method == "POST":

        form_inicio = AuthenticationForm(request, data = request.POST)
        
        if form_inicio.is_valid():

            info = form_inicio.cleaned_data
            usuario = info.get("username")
            contrasena = info.get("password")

            
            user = authenticate(username=usuario, password=contrasena)

            if user:
                login(request, user)  
                return render(request, "appweb/inicio.html", {'mensaje': f"Bienvenido {user}"})
        
        else:
            return render(request,"appweb/inicio.html", {"mensaje":"Usuario Incorrecto"})
    else:
        
        form_inicio = AuthenticationForm()

    return render(request,"appweb/login.html", {"form":form_inicio} )

def register(request):

    if request.method == 'POST':

            
            form = UserRegisterForm(request.POST)
            if form.is_valid():

                username = form.cleaned_data['username']
                form.save()
                return render(request,"appweb/inicio.html" ,  {"mensaje":"Usuario Creado :)"})

    else:
            #form = UserCreationForm()       
            form = UserRegisterForm()     

    return render(request,"appweb/register.html" ,  {"form":form})

@login_required
def agregarAvatar(request):
    if request.method == 'POST':
        miFormulario = AvatarFormulario(request.POST, request.FILES)
        if miFormulario.is_valid():
            usuario = request.user
            imagen = miFormulario.cleaned_data['imagen']
            avatar = Avatar(user=usuario, imagen=imagen)
            avatar.save()

            return render(request, "appweb/inicio.html")

    else:
        miFormulario = AvatarFormulario()
    
    return render(request, "appweb/agregarAvatar.html", {"miFormulario": miFormulario})

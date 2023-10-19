from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

# Create your views here.

def register(request):

    if request.method == 'POST':

            
            form = RegistroFormulario(request.POST)
            if form.is_valid():

                user = form.cleaned_data['username']
                form.save()
                return render(request,"appweb/inicio.html" ,  {"mensaje": "Usuario Creado"})

    else:   
            form = RegistroFormulario()     

    return render(request,"appweb/Autenticar/register.html" ,  {"form":form})

def login_request(request):

    if request.method == "POST":

        form = AuthenticationForm(request, data = request.POST)
        
        if form.is_valid():

            usuario = form.cleaned_data.get("username")
            contrasena = form.cleaned_data.get("password")

            
            user = authenticate(username=usuario, password=contrasena)

            if user:
                login(request, user)  
                return render(request, "appweb/inicio.html", {'mensaje': f"Bienvenido {user}"})
        
        else:
            return render(request,"appweb/inicio.html", {"mensaje": "Usuario Incorrecto"})
    else:
        
        form = AuthenticationForm()

    return render(request,"appweb/Autenticar/login.html", {"form":form} )


def inicio(request):
    return render(request, "appweb/inicio.html")

def producto(request):
    
    todos = Producto.objects.all()

    return render(request, "appweb/producto.html",{"producto": todos})

def comentario(request):
    return render(request, "appweb/comentario.html")

@login_required
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

@login_required
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

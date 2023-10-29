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

@login_required
def EditarUsuario(request):

    usuario = request.user 

    if request.method == "POST":    

        miFormulario = RegistroFormulario(request.POST) 

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data     

            usuario.username = informacion['username']
            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password1']
            usuario.save()

            return render(request, "appweb/inicio.html")

    else:

        miFormulario= RegistroFormulario(initial={'username':usuario.username, 'email':usuario.email})

    return render(request, "appweb/Autenticar/editar_usuario.html",{'miFormulario':miFormulario, 'usuario':usuario.username})


def about(request):
    return render(request, 'appweb/about.html')

def inicio(request):
    return render(request, "appweb/inicio.html")

@login_required
def registroProducto(request):
    
    if request.method == "POST":
        
        miFormulario = ProductoFormulario(request.POST, request.FILES)
        
        if miFormulario.is_valid():
            
            informacion = miFormulario.cleaned_data
            
            ProductoNuevo = Producto(nombre=informacion["nombre"], descripcion=informacion["descripcion"],precio=informacion["precio"],stock=informacion["stock"],imagen=informacion["imagen"],)
            ProductoNuevo.save()
            
            return render(request, "appweb/inicio.html")
    else:
        miFormulario = ProductoFormulario()
        
    return render(request, "appweb/productos/registro_producto.html", {"form": miFormulario})

@login_required
def producto(request):
    
    productos = Producto.objects.all()

    return render(request, "appweb/productos/productos.html",{"resultado_producto": productos})

@login_required
def eliminarProducto(request, producto_nombre):

    producto = Producto.objects.get(nombre=producto_nombre)
    
    producto.delete()
    
    producto = Producto.objects.all()

    return render(request, "appweb/productos/productos.html",{"resultado_producto": producto})

@login_required
def editarProducto(request,producto_nombre):

    producto = Producto.objects.get(nombre=producto_nombre)

    if request.method == "POST":

        miFormulario = ProductoFormulario(request.POST, request.FILES)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data
            
            producto.nombre = informacion['nombre']
            producto.descripcion = informacion['descripcion']
            producto.precio = informacion['precio']
            producto.stock = informacion['stock']
            producto.imagen = informacion['imagen']
            

            producto.save()

            return render(request, "appweb/inicio.html")

    else:

        miFormulario= ProductoFormulario(initial={'nombre':producto.nombre, 'descripcion':producto.descripcion,'precio':producto.precio, 'stock':producto.stock, 'imagen':producto.imagen})

    return render(request, "appweb/productos/editar_producto.html",{"miFormulario":miFormulario, "resultado_producto": producto})

@login_required
def Buscar_Producto(request):

    if request.GET["producto"]:

        nombre=request.GET['producto']

        resultados=Producto.objects.filter(nombre__icontains=nombre)

        return render(request, "appweb/productos/resultados_busqueda.html",{"resultados":resultados, "busqueda_producto":nombre})

    else:

        respuesta="No enviaste datos."

    return HttpResponse(respuesta)
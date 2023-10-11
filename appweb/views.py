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

@login_required
def cliente(request):
    
    todos = Cliente.objects.all()
    
    return render(request, "appweb/cliente.html", {"cliente": todos})

def vendedor(request):
    return render(request, "appweb/vendedor.html")

def producto(request):
    return render(request, "appweb/producto.html")

def comentario(request):
    return render(request, "appweb/comentario.html")


def registroCliente(request):
    
    if request.method == "POST":
        
        miFormulario = ClienteFormulario(request.POST)
        
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            clienteNuevo = Cliente(nombre=informacion["nombre"], apellido=informacion["apellido"],rut=informacion["rut"],direccion=informacion["direccion"],email=informacion["email"],)
            clienteNuevo.save()
            return render(request, "appweb/inicio.html")
    else:
        miFormulario = ClienteFormulario()
        
    return render(request, "appweb/registro_cliente.html", {"form": miFormulario})

def buscarCliente(request):

    return render(request, "appweb/buscar_cliente.html")

def resultadoCliente(request):

    if request.GET["nombre"]:

        nombre = request.GET["nombre"]
        clienteresultado = Cliente.objects.filter(nombre__icontains=nombre)

        return render(request, "appweb/resultado_cliente.html", {"valor": nombre, "res": clienteresultado})
    else:
        return HttpResponse("No enviaste Datos.")

    return render(request, "appweb/resultado_cliente.html")

def eliminarCliente(request, cliente_id):
    clienteEliminado = Cliente.objects.get(id= cliente_id)
    clienteEliminado.delete()
    todos = Cliente.objects.all()

    return render(request, "appweb/cliente.html", {"cliente": todos})

def actualizarCliente(request,cliente_nombre):
    
    clienteElegido = Cliente.objects.get(nombre=cliente_nombre)
    
    if request.method == "POST":
        
        miFormulario = ClienteFormulario(request.POST)
        
        if miFormulario.is_valid():
            
            informacion = miFormulario.cleaned_data
            
            clienteElegido.nombre = informacion["nombre"]
            clienteElegido.apellido = informacion["apellido"]
            clienteElegido.rut = informacion["rut"]
            clienteElegido.direccion = informacion["direccion"]
            clienteElegido.email = informacion["email"]
            
            clienteElegido.save()
            
            return render(request, "appweb/inicio.html")
    else:
        miFormulario = ClienteFormulario(initial={"nombre": clienteElegido.nombre,
                                                "apellido": clienteElegido.apellido,
                                                "rut": clienteElegido.rut,
                                                "direccion": clienteElegido.direccion,
                                                "email": clienteElegido.email})
        
    return render(request, "appweb/registro_cliente.html", {"form": miFormulario})

def login_view(request):

    if request.method == "POST":

        form_inicio = AuthenticationForm(request, data = request.POST)
        
        if form_inicio.is_valid():

            info = form_inicio.cleaned_data
            usuario = info.get("username")
            contrasena = info.get("password")

            #acá hacemos la validación
            user = authenticate(username=usuario, password=contrasena)

            if user:
                login(request, user)  
                return render(request, "appweb/inicio.html", {"usuario":user})
        
        else:
            return render(request,"appweb/inicio.html", {"mensaje":"usuario invalido"})

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
def editarPerfil(request):

    usuario = request.user

    if request.method == 'POST':

        miFormulario = UserEditForm(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.last_name = informacion['last_name']
            usuario.first_name = informacion['first_name']

            usuario.save()

            return render(request, "appweb/inicio.html")

    else:

        miFormulario = UserEditForm(initial={'email': usuario.email})

    return render(request, "appweb/editarPerfil.html", {"miFormulario": miFormulario, "usuario": usuario})

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

class ClienteLista(ListView): #estudiante_list.html
    model = Cliente
    template_name = "appweb/lista_cliente.html"
#Detail 
class ClienteDetalle(DetailView): #estudiante_detail.html
    model = Cliente
    
#Create
class ClienteCrear(CreateView): #estudiante_form.html
    model = Cliente
    fields = ["nombre", "apellido","rut","direccion","email"]
    success_url = "/appweb/cliente/lista/"

#Update
class ClienteActualizar(UpdateView): #estudiante_form.html
    model = Cliente
    fields = ["nombre", "apellido", "email"]
    success_url = "/appweb/cliente/lista/"

#Delete
class ClienteBorrar(DeleteView): #estudiante_confirm_delete.html
    model = Cliente 
    success_url = "/appweb/cliente/lista/"
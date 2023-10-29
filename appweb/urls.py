from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView



urlpatterns = [
    #el inicio de la pagina
    path('inicio',inicio,name="Inicio"),
    path('about',about,name="about"),
    path('buscar/', Buscar_Producto),
    
    #login inicio de sesion
    path('login',login_request, name="Login"),
    path('logout', LogoutView.as_view(template_name='appweb/Autenticar/logout.html'), name="Logout"),
    path("register",register, name="Register"),
    
    #productos
    path("AgregarProducto",registroProducto, name="AgregarProducto"),
    path("Productos", producto , name="Productos"),
    path("EditarProductos/<producto_nombre>", editarProducto, name="EditarProductos"),
    path("BorrarProductos/<producto_nombre>", eliminarProducto, name="BorrarProductos"),
]
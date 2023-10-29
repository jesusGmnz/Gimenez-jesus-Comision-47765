from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView



urlpatterns = [
    #el inicio de la pagina
    path('inicio',inicio,name="Inicio"),
    path('about',about,name="about"),
    
    #buscar los productos creados
    path('buscar/', Buscar_Producto),
    
    #login inicio de sesion
    path('login',login_request, name="Login"),
    path('logout', LogoutView.as_view(template_name='appweb/Autenticar/logout.html'), name="Logout"),
    path("register",register, name="Register"),
    path("EditarUsuario", EditarUsuario, name="EditarUsuario"),
    
    #productos CRUD
    path("AgregarProducto",registroProducto, name="AgregarProducto"), #crear un producto
    path("Productos", producto , name="Productos"), #ver los productos creados
    path("EditarProductos/<producto_nombre>", editarProducto, name="EditarProductos"), #modificar los productos
    path("BorrarProductos/<producto_nombre>", eliminarProducto, name="BorrarProductos"), #eliminar algun producto
    
]
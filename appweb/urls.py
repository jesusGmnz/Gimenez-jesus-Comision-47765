from django.urls import path
from .views import *



urlpatterns = [
    #el inicio de la pagina
    path('inicio/',inicio,name="Inicio"),
    
    #url para leer
    path('Producto/',producto,name="Producto"),
    path('comentario/',comentario,name="Comentario"),
        
    #los crud de producto
    path('registroProducto/',registroProducto, name="registroProducto" ),
    path('borrarProducto/<int:producto_id>/',eliminarProducto, name="borrarProducto"),
    path('editaProducto/<producto_nombre>/',actualizarProducto, name='editarProducto'),
    
    #buscar producto
    path('buscarProducto/',buscarProducto,name="buscarProducto"),
    
    #resultado de la busqueda
    path('resultadoProducto/',resultadoProducto,name="resultadoProducto"),
    
    #comentario
    path('agregarComentario/',agregarComentario,name="agregarComenterio"),
    
    #login inicio de sesion
    path("login/",login_view, name="Login"),
    path("register/",register, name="Register"),

    path('agregarAvatar/',agregarAvatar, name="AgregarAvatar"),
    path('logout/',LogoutView.as_view(template_name='appweb/logout.html'), name='Logout'),
    

]
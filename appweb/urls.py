from django.urls import path
from .views import *



urlpatterns = [
    #el inicio de la pagina
    path('inicio/',inicio,name="Inicio"),
    
    #url para leer
    path('vendedor/',vendedor,name="Vendedor"),
    path('podructo/',producto,name="Producto"),
    path('comentario/',comentario,name="Comentario"),
        
    #los crud de cliente
    path('cliente/',cliente,name="Cliente"),
    path('registroCliente',registroCliente, name="registroCliente" ),
    path('borrarCliente/<int:cliente_id>/',eliminarCliente, name="borrarCliente"),
    path('editarCliente/<cliente_nombre>/',actualizarCliente, name='editarCliente'),
    #buscar cliente
    path('buscarCliente',buscarCliente,name="buscarCliente"),
    #resultado de la busqueda
    path('resultadoCliente',resultadoCliente,name="resultadoCliente"),
    
    #login inicio de sesion
    path("login/",login_view, name="Login"),
    path("register/",register, name="Register"),
    path('editarPerfil/',editarPerfil, name="EditarPerfil"),
    path('agregarAvatar/',agregarAvatar, name="AgregarAvatar"),
    path('logout',LogoutView.as_view(template_name='appweb/logout.html'), name='Logout'),
    
    #crud cliente vistas usando clases
    path("cliente/lista/", ClienteLista.as_view(), name="Ver Cliente"),
    path("cliente/detalle/<int:pk>", ClienteDetalle.as_view(), name="Detalle cliente"),
    path("cliente/nuevo/", ClienteCrear.as_view(), name="Crear Cliente"),
    path("cliente/actualizar/<int:pk>", ClienteActualizar.as_view(), name="Actualizar Cliente"),
    path("cliente/borrar/<int:pk>", ClienteBorrar.as_view(), name="Borrar Cliente"),

]
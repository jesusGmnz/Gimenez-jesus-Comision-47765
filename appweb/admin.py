from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Vendedor)
admin.site.register(Producto)
admin.site.register(Comentario)
admin.site.register(Avatar)
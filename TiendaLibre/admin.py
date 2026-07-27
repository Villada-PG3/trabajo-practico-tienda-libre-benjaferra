from django.contrib import admin
from .models import Producto
from .models import categoria

# Registrar el modelo Producto en el admin
admin.site.register(Producto)
admin.site.register(categoria)
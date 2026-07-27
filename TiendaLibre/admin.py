from django.contrib import admin
from .models import Producto

# Registrar el modelo Producto en el admin
admin.site.register(Producto)
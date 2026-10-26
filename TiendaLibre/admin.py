from django.contrib import admin
from .models import Producto
from .models import Categoria
from django.utils.html import format_html

admin.site.register(Categoria)

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    # Definimos qué columnas mostrar en la lista
    list_display = ('mostrar_imagen', 'nombre', 'precio')

    # Función para renderizar el HTML de la imagen
    @admin.display(description='Imagen')
    def mostrar_imagen(self, obj):
        if obj.imagen:
            return format_html(
                '<img src="{}" style="width: 50px; height: 50px; object-fit: cover; border-radius: 6px;" />',
                obj.imagen.url,
            )
        return 'Sin imagen'
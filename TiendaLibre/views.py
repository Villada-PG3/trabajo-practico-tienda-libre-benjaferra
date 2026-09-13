from tkinter import NO
from .models import Producto
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views.generic import TemplateView

class HolaTemplateView(TemplateView):
    
    template_name = 'hola.html'


def home(request):
    productos = Producto.objects.filter(activo=True).order_by('-fecha_creacion')[:3]
    context = {'productos': productos, 'titulo': 'Ultimas novedades', 'usuario_logueado': True,}
    return render(request, 'tiendalibre/home.html', context)

def catalogo(request):
    productos = Producto.objects.filter(activo=True).order_by('categoria', 'nombre')
    context = {'productos': productos}
    return render(request, 'tiendalibre/catalogo.html', context)

def acerca_de_mi(request):
    return render(request, 'tiendalibre/acerca-de-mi.html')


# ... tus otras vistas ...
def detalle_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    return render(
        request, 'tiendalibre/detalle_producto.html', {'producto': producto}
    )
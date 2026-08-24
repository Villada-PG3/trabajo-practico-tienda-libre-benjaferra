from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

class HolaTemplateView(TemplateView):
    
    template_name = 'hola.html'


def home(request):
    return render(request, 'tiendalibre/home.html')

def acerca_de_mi(request):
    return render(request, 'tiendalibre/acerca-de-mi.html')

def home(request):
    productos_destacados = [
        {'nombre': 'Producto 1', 'precio': 10.99},
        {'nombre': 'Producto 2', 'precio': 19.99},
        {'nombre': 'Producto 3', 'precio': 5.99},
    ]

    context = {
        'titulo': 'Productos de la semana',
        'productos': productos_destacados,
        'usuario_logueado': False
    }
    return render(request, 'tiendalibre/home.html', context)


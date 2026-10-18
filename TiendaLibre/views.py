from tkinter import NO
from .models import Producto
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView

class HolaTemplateView(TemplateView):
    
    template_name = 'hola.html'


def acerca_de_mi(request):
    return render(request, 'tiendalibre/acerca-de-mi.html')


# ... tus otras vistas ...
def detalle_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    return render(
        request, 'tiendalibre/detalle_producto.html', {'producto': producto}
    )

class HomeView(TemplateView):
    template_name = 'tiendalibre/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo_pagina'] = 'TiendaLibre - Inicio'
        context['usuario'] = 'Benjamin'
        context['productos_destacados'] = Producto.objects.all().order_by('-fecha_creacion')[:6]
        return context


class CatalogoView(ListView):
    model = Producto
    template_name = 'tiendalibre/catalogo.html'
    context_object_name = 'productos'  # Nombre con el que se iterará en el template (en lugar de object_list)
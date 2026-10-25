from tkinter import NO
from .models import Producto
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView

class HolaTemplateView(TemplateView):
    
    template_name = 'hola.html'


def acerca_de_mi(request):
    return render(request, 'tiendalibre/acerca-de-mi.html')


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
    context_object_name = 'productos'
    paginate_by = 6 


class ProductoDetailView(DetailView):
    model = Producto
    template_name = 'tiendalibre/detalle_producto.html'
    context_object_name = 'producto' 
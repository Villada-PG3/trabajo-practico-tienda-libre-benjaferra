from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView, ListView, TemplateView
from .models import Categoria, Producto


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
    context['productos_destacados'] = (
        Producto.objects.all().order_by('-fecha_creacion')[:6]
    )
    return context


class ProductoDetailView(DetailView):
  model = Producto
  template_name = 'tiendalibre/detalle_producto.html'
  context_object_name = 'producto'


class CatalogoView(ListView):
  model = Producto
  template_name = 'tiendalibre/catalogo.html'
  context_object_name = 'productos'
  paginate_by = 6

  def get_queryset(self):
    queryset = super().get_queryset()
    query = self.request.GET.get('q')
    if query:
      queryset = queryset.filter(nombre__icontains=query)
    return queryset


class CategoriaView(ListView):
  model = Producto
  template_name = 'tiendalibre/categoria.html'
  context_object_name = 'productos'
  paginate_by = 6

  def get_queryset(self):
    self.categoria = get_object_or_404(
        Categoria, slug=self.kwargs.get('slug')
    )
    return Producto.objects.filter(categoria=self.categoria)

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['categoria'] = self.categoria
    return context
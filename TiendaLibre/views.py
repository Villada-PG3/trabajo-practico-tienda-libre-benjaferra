from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

class HolaTemplateView(TemplateView):
    
    template_name = 'hola.html'


def home(request):
    productos_destacados = [
        {'nombre': 'Auriculares Sony WH-1000XM5', 'marca': 'Sony', 'descripcion': 'Cancelación de ruido y hasta 30 horas de batería.', 'precio': 349.99, 'stock': 8},
        {'nombre': 'iPhone 15', 'marca': 'Apple', 'descripcion': 'Pantalla Super Retina XDR y cámara principal de 48 MP.', 'precio': 799.00, 'stock': 0},
        {'nombre': 'Notebook Galaxy Book4', 'marca': 'Samsung', 'descripcion': 'Laptop liviana con procesador Intel Core y pantalla Full HD.', 'precio': 949.99, 'stock': 4},
        {'nombre': 'Nintendo Switch OLED', 'marca': 'Nintendo', 'descripcion': 'Consola híbrida con pantalla OLED de 7 pulgadas.', 'precio': 349.99, 'stock': 0},
        {'nombre': 'Cafetera Nespresso Essenza Mini', 'marca': 'Nespresso', 'descripcion': 'Café espresso en cápsulas con diseño compacto.', 'precio': 129.90, 'stock': 12},
        {'nombre': 'Zapatillas Air Max 270', 'marca': 'Nike', 'descripcion': 'Amortiguación visible y comodidad para todos los días.', 'precio': 159.99, 'stock': 3},
    ]

    context = {
        'titulo': 'Productos de la semana',
        'productos': productos_destacados,
        'usuario_logueado': False
    }
    return render(request, 'tiendalibre/home.html', context)


def acerca_de_mi(request):
    return render(request, 'tiendalibre/acerca-de-mi.html')


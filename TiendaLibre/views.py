from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

class HolaTemplateView(TemplateView):
    
    template_name = 'hola.html'


def home(request):
    return render(request, 'tiendalibre/home.html')

def acerca_de_mi(request):
    return render(request, 'tiendalibre/acerca-de-mi.html')
    
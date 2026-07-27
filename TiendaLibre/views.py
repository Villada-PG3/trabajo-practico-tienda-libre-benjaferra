from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

class HolaTemplateView(TemplateView):
    
    template_name = 'hola.html'
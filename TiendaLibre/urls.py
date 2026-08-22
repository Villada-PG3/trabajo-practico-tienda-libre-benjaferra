from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('acerca-de-mi/', views.acerca_de_mi, name='acerca_de_mi'),
]


urlpatterns = [
    path('', views.home, name='home'),
    # Cambia views.acerca_de por views.acerca_de_mi:
    path('acerca-de-mi/', views.acerca_de_mi, name='acerca_de'),
]
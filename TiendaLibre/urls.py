from django.urls import path
from .views import HomeView, CatalogoView, acerca_de_mi, detalle_producto 

urlpatterns = [
    # Mapeo a CBV usando .as_view()
    path('', HomeView.as_view(), name='home'),
    path('catalogo/', CatalogoView.as_view(), name='catalogo'),
    
    # Rutas existentes
    path('acerca-de-mi/', acerca_de_mi, name='acerca_de_mi'),
    path('producto/<int:pk>/', detalle_producto, name='detalle_producto'),
]
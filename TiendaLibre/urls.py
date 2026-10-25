from django.urls import path
from .views import HomeView, CatalogoView, ProductoDetailView, acerca_de_mi


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('catalogo/', CatalogoView.as_view(), name='catalogo'),
    path('acerca-de-mi/', acerca_de_mi, name='acerca_de'),
    
    # Ruta de detalle actualizada a CBV
    path('producto/<int:pk>/', ProductoDetailView.as_view(), name='detalle_producto'),
]
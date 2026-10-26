from django.urls import path
from .views import (
    CatalogoView,
    CategoriaView,
    HomeView,
    ProductoDetailView,
    acerca_de_mi,
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('catalogo/', CatalogoView.as_view(), name='catalogo'),
    path('categoria/<slug:slug>/', CategoriaView.as_view(), name='categoria_detalle'),
    path('acerca-de-mi/', acerca_de_mi, name='acerca_de'),
    path(
        'producto/<int:pk>/',
        ProductoDetailView.as_view(),
        name='detalle_producto',
    ),
]
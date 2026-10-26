from .models import Categoria


def categorias_processor(request):
    """Devuelve todas las categorías para ser usadas globalmente en templates"""
    return {'categorias_globales': Categoria.objects.all()}
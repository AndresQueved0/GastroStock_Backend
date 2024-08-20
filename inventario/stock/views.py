from django.shortcuts import get_object_or_404, render
from .models import inventario  # Asegúrate de que el modelo se llame 'inventario'

def inventario_list(request):
    productos = inventario.objects.all()
    return render(request, 'stock/list/list.html', {'productos': productos})


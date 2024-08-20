from django.contrib import admin
from .models import inventario

@admin.register(inventario)
class InventarioAdmin(admin.ModelAdmin):
    list_display = ('nombre_producto', 'cantidad', 'precio_unitario', 'categoria')
    list_filter = ('categoria',)
    search_fields = ('nombre_producto', 'descripcion')
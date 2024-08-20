from django import forms
from stock.models import inventario

class ProductoForm(forms.ModelForm):
    class Meta:
        model = inventario
        fields = ['nombre_producto', 'descripcion', 'cantidad', 'precio_unitario', 'categoria', 'fecha_expiracion']
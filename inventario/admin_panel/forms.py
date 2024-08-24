from django import forms
from stock.models import inventario
from django.contrib.auth.forms import AuthenticationForm
from .models import CustomUser

class CustomLoginForm(AuthenticationForm):
    user_type = forms.ChoiceField(choices=CustomUser.USER_TYPE_CHOICES, required=True, label='Tipo de Usuario')

    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'user_type']

class ProductoForm(forms.ModelForm):
    class Meta:
        model = inventario
        fields = ['nombre_producto', 'descripcion', 'cantidad', 'precio_unitario', 'categoria', 'fecha_expiracion']
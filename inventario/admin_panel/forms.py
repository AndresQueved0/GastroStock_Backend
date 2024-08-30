from django import forms
from stock.models import inventario
from django.contrib.auth.forms import AuthenticationForm
from .models import CustomUser

class CustomLoginForm(AuthenticationForm):
    user_type = forms.ChoiceField(
        choices=CustomUser.USER_TYPE_CHOICES, 
        required=True, 
        label='Tipo de Usuario',
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'user_type']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['password'].widget.attrs.update({'class': 'form-control'})

class ProductoForm(forms.ModelForm):
    class Meta:
        model = inventario
        fields = ['nombre_producto', 'descripcion', 'cantidad', 'precio_unitario', 'categoria', 'fecha_expiracion']
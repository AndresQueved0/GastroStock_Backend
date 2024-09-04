from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import CustomUser
from .models import Inventario
from django.utils import timezone

# Formulario de autenticación personalizado

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

# Formulario de registro producto personalizado

class InventarioForm(forms.ModelForm):
    class Meta:
        model = Inventario
        fields = ['nombre_producto', 'descripcion', 'cantidad', 'precio_unitario', 'categoria', 'fecha_expiracion', 'fecha_entrada']
        widgets = {
            'nombre_producto': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
            'precio_unitario': forms.NumberInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'fecha_expiracion': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'fecha_entrada': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Establecer la fecha actual como valor inicial para fecha_entrada
        self.fields['fecha_entrada'].initial = timezone.now().date()
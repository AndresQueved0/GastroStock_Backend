from django.shortcuts import render, redirect,  get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from stock.models import inventario
from .forms import ProductoForm
from .forms import CustomLoginForm

@login_required
def admin_dashboard(request):
    productos = inventario.objects.all()
    context = {
        'productos': productos,
    }
    return render(request, 'admin_panel/dashboard.html', context)

@login_required
def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = ProductoForm()
    return render(request, 'admin_panel/agregar_producto.html', {'form': form})

@login_required
def borrar_producto(request, producto_id):
    producto = get_object_or_404(inventario, id=producto_id)
    if request.method == 'POST':
        producto.delete()
        return redirect('admin_dashboard')
    return render(request, 'admin_panel/confirmar_borrar.html', {'producto': producto})

def admin_login(request):
    if request.method == 'POST':
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user_type = form.cleaned_data.get('user_type')
            user = authenticate(username=username, password=password)
            if user is not None and user.user_type == user_type:
                login(request, user)
                return redirect(reverse('admin_dashboard'))
            else:
                form.add_error(None, "Credenciales inválidas o tipo de usuario incorrecto.")
    else:
        form = CustomLoginForm()
    return render(request, 'admin_panel/login.html', {'form': form})
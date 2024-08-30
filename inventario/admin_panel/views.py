from django.shortcuts import render, redirect,  get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from stock.models import inventario
from .forms import ProductoForm
from .forms import CustomLoginForm
from django.contrib import messages

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
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if user.user_type == user_type:
                    login(request, user)
                    if user_type == 'admin':
                        return redirect('admin_dashboard')
                    elif user_type == 'meseros':
                        return redirect('meseros_dashboard')
                    elif user_type == 'cocina':
                        return redirect('cocina_dashboard')
                    elif user_type == 'caja':
                        return redirect('caja_dashboard')
                else:
                    messages.error(request, "Tipo de usuario incorrecto para estas credenciales.")
            else:
                messages.error(request, "Usuario o contraseña incorrectos.")
    else:
        form = CustomLoginForm()
    return render(request, 'login.html', {'form': form})

@login_required
def admin_dashboard(request):
    return render(request, 'admin_panel/admin_dashboard.html')

@login_required
def meseros_dashboard(request):
    return render(request, 'admin_panel/meseros_dashboard.html')

@login_required
def cocina_dashboard(request):
    return render(request, 'admin_panel/cocina_dashboard.html')

@login_required
def caja_dashboard(request):
    return render(request, 'admin_panel/caja_dashboard.html')
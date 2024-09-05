from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Inventario, Categoria
from .forms import InventarioForm, CustomLoginForm
from django.urls import reverse
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods


@login_required
def admin_dashboard(request):
    productos = Inventario.objects.all()
    context = {
        'productos': productos,
    }
    return render(request, 'admin_panel/admin_dashboard.html', context)

@login_required
def agregar_producto(request):
    if request.method == 'POST':
        form = InventarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto agregado exitosamente.')
            return redirect(reverse('admin_dashboard'))  # Usamos reverse() para generar la URL
    else:
        form = InventarioForm()
    return render(request, 'admin_panel/agregar_producto.html', {'form': form})

@login_required
def borrar_producto(request, producto_id):
    producto = get_object_or_404(Inventario, id=producto_id)
    if request.method == 'POST':
        producto.delete()
        messages.success(request, 'Producto eliminado exitosamente.')
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
    productos = Inventario.objects.all()
    context = {
        'productos': productos,
    }
    return render(request, 'admin_panel/admin_dashboard.html', context)

@login_required
def meseros_dashboard(request):
    productos = Inventario.objects.filter(cantidad__gt=0)
    context = {
        'productos': productos,
    }
    return render(request, 'admin_panel/meseros_dashboard.html', context)

@login_required
def cocina_dashboard(request):
    productos = Inventario.objects.all()
    context = {
        'productos': productos,
    }
    return render(request, 'admin_panel/cocina_dashboard.html', context)

@login_required
def caja_dashboard(request):
    productos = Inventario.objects.all()
    context = {
        'productos': productos,
    }
    return render(request, 'admin_panel/caja_dashboard.html', context)


    
@require_http_methods(["POST"])
def borrar_producto(request, producto_id):
    producto = get_object_or_404(Inventario, id=producto_id)
    try:
        producto.delete()
        return JsonResponse({'success': True})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})
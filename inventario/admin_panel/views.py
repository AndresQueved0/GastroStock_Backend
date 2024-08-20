from django.shortcuts import render, redirect,  get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from stock.models import inventario
from django.views.decorators.csrf import csrf_exempt
from .forms import ProductoForm

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

@csrf_exempt
def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse('admin_dashboard'))
        else:
            error_message = "Usuario o contraseña incorrectos."
    else:
        error_message = ""
    
    return render(request, 'admin_panel/login.html', {'error_message': error_message})
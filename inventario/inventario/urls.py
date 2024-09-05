"""
URL configuration for inventario project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from admin_panel import views as admin_panel_views
from admin_panel import views

urlpatterns = [
    path('', admin_panel_views.admin_login, name='login'),
    path('admin-panel/', include('admin_panel.urls')),
    path('agregar-producto/', views.agregar_producto, name='agregar_producto'),
    path('admin/', views.admin_dashboard, name='admin_dashboard'),
    path('meseros/', views.meseros_dashboard, name='meseros_dashboard'),
    path('cocina/', views.cocina_dashboard, name='cocina_dashboard'),
    path('caja/', views.caja_dashboard, name='caja_dashboard'),
    path('borrar-producto/<int:producto_id>/', views.borrar_producto, name='borrar_producto'),
    path('admin-panel/', include('admin_panel.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
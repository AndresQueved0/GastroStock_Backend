from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_dashboard, name='admin_dashboard'),  # Asegúrate de que esta línea esté presente
    path('dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('login/', views.admin_login, name='admin_login'),
    path('agregar-producto/', views.agregar_producto, name='agregar_producto'),
    path('admin/', views.admin_dashboard, name='admin_dashboard'),
    path('meseros/', views.meseros_dashboard, name='meseros_dashboard'),
    path('cocina/', views.cocina_dashboard, name='cocina_dashboard'),
    path('caja/', views.caja_dashboard, name='caja_dashboard'),
    path('borrar-producto/<int:producto_id>/', views.borrar_producto, name='borrar_producto'),
]
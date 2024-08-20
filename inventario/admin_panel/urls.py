from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_dashboard, name='admin_dashboard'),  # Asegúrate de que esta línea esté presente
    path('login/', views.admin_login, name='admin_login'),
    path('agregar_producto/', views.agregar_producto, name='agregar_producto'),
    path('borrar_producto/<int:producto_id>/', views.borrar_producto, name='borrar_producto'),
]
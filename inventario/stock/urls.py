from django.urls import path
from . import views

app_name = 'stock'

urlpatterns = [
    path('', views.inventario_list, name='inventario_list'),
    
]


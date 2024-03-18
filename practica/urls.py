from django.urls import path
from . import views

urlpatterns = [
    path('verformulario', views.see_product, name='productoSee'),
    path('guardarformulario', views.crear_producto, name='productoCreate'),
]
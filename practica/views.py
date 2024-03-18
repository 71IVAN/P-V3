from django.shortcuts import redirect, render
from practica.models import Producto
from .forms import ProductoForm

# Create your views here.
from django.shortcuts import render
from .forms import ProductoFormset

def see_product(request):

    productos = Producto.objects.all()
    return render(request, 'components/forms/components-formpractica.html', {'productos': productos})

def crear_producto(request):
    if request.method == 'POST':
        formset = ProductoFormset(request.POST)
        if formset.is_valid():
            formset.save()  # Guardar todos los formularios del formset a la vez
            return redirect('ruta_a_redirigir')  # Redirigir a una página después de guardar los datos
    else:
        formset = ProductoFormset()
    return render(request, 'crear_producto.html', {'formset': formset})


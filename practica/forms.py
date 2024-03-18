from django import forms 
from .models import Producto
from django.forms import formset_factory

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'

ProductoFormset = formset_factory(ProductoForm, extra=3)

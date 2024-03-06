from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Field, Layout
from .models import ModelThird

class thirdForms(forms.ModelForm):

    class Meta:
        model = ModelThird
        #fields = ['name', 'email', 'address'] #Defino orden 
        fields = '__all__' #me incluye todos los campos creados en el modelo y respeta su orden

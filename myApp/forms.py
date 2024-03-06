from django import forms
from .models import modeltest

class myForm(forms.ModelForm):
     
    class Meta:
        model = modeltest
        fields = '__all__'

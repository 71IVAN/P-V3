from django import forms
from .models import ModelThird

class ThirdForm(forms.ModelForm):
    class Meta:
        model = ModelThird
        fields = '__all__'   

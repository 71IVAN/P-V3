from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit
from .models import ModelThird

class ThirdForm(forms.ModelForm):
    class Meta:
        model = ModelThird
        fields = '__all__'   

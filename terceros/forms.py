from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit
from .models import ModelThird


class ThirdForm(forms.ModelForm):
    name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Name', 'class': 'form-control'}),
        help_text="ejm: Alexander Anderson"
    )
    
    email = forms.EmailField(
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Email', 'class': 'form-control'}),
        help_text="ejm: name@example.com"
    )
    
    phone = forms.IntegerField(
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Phone', 'class': 'form-control'}),
        help_text="ejm: 3205443311"
    )
    
    identity_document = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Identity Document', 'class': 'form-control'}),
        help_text="ejm: 123409"
    )

    
    class Meta:
        model = ModelThird
        fields = '__all__'   
        exclude = ['hora']
        
        

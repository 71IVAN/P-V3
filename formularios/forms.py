from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from .models import third

from .models import MiModelo

class formThird(forms.ModelForm):
    class Meta:
        model = third
        fields = ['firstName', 'lastName', 'phone','email','address','thirdsPartyType']  # Lista los campos que quieres en tu formulario

    def __init__(self, *args, **kwargs):
        super(formThird, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'firstName', 
            'lastName',
            'phone',
            'email',
            'address',
            'thirdsPartyType',
            Submit('submit', 'Enviar', css_class='btn-success')
        )

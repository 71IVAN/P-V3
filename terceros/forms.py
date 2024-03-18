from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from .models import ModelThird

class ThirdForm(forms.ModelForm):
    class Meta:
        model = ModelThird
        fields = '__all__'
        
    # def __init__(self, *args, **kwargs):
    #     super(ThirdForm, self).__init__(*args, **kwargs)
    #     self.helper = FormHelper()
    #     self.helper.form_method = 'post'
    #     self.helper.add_input(Submit('submit', 'Submit'))     

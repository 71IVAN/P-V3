from django.contrib.auth.models import User
from django import forms

class formUser(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        exclude = ['password', 'date_joined']
        
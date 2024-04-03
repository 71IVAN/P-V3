from django import forms
from .models import modelBoostrap

class FormBootstrap(forms.ModelForm):
    class Meta:
        model = modelBoostrap
        fields = '__all__'

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) <= 3:
            raise forms.ValidationError("Name must be at least 3 characters long")
        return name

    def clean_email(self):
        email = self.cleaned_data['email']
        allowed_domains = ['com', '.net', '.in', '.org']
        domain = email.split('.')[-1]
        if domain not in allowed_domains:
            raise forms.ValidationError("Email is not valid")
        return email 

    def clean_ide(self):
        ide = self.cleaned_data['ide']
        if len(ide) < 5:
            raise forms.ValidationError("Identity document must be at least 5 characters long")
        return ide

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if len(phone) != 10:
            raise forms.ValidationError("Phone number must have 10 digits.")
        return phone

    def clean_address(self):
        address = self.cleaned_data['address']
        if len(address) <= 10:
            raise forms.ValidationError("Address must be at least 10 characters long")
        return address

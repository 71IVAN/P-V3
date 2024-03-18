from django import forms
from .models import modeltest

class myForm(forms.ModelForm):

    class Meta:
        model = modeltest
        fields = '__all__'
    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        if len(nombre) <= 3:
            raise forms.ValidationError("Name must be at least 3 characters long")
        return nombre
    
    def clean_email(self):
        email = self.cleaned_data['email']
        allowed_domians = ['com', '.net', '.in', '.org']
        if not any(email.endswith(domain) for domain in allowed_domians):
            raise forms.ValidationError("Email its not valid") 
        return email
    
    def clean_telefono(self):
        telefono = self.cleaned_data['telefono']
        if len(telefono) > 10:
            raise forms.ValidationError("Phone number must have 10 digits.")
        return telefono
    
    def clean_address(self):
        address = self.cleaned_data['address']
        if len(address) < 10:
            raise forms.ValidationError("Address must be at least 5 characters long")
        return address
    
    def clean_typeThird(self):
        typeThird = self.cleaned_data['typeThird']
        if len(typeThird) < 5:
            raise forms.ValidationError("Type must be at least 5 characters long")
        return typeThird
    
    def clean_identity_document(self):
        identity_document = self.cleaned_data['identity_document']
        if len(identity_document) < 5:
            raise forms.ValidationError("Identity document must be at least 5 characters long")
        return identity_document
   
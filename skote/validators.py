from django import forms
from django.core import validators

from django.contrib.auth.models import User

class NameValidator(validators.RegexValidator):
    def __call__(self,value):
        if len(value) <= 3:
            raise forms.ValidationError("El nombre debe tener al menos 3 caracteres")
        if value.isdigit():
            raise forms.ValidationError("El nombre no puede ser numerico")        
        return value

class EmailDomainValidator(validators.RegexValidator):
     def __call__(self, value):
        allowed_domains = ['com', '.net', '.in', '.org']
        if not any(value.endswith(domain) for domain in allowed_domains):
            raise forms.ValidationError("El correo electrónico no es válido. Por favor, ingrese un dominio válido.")
        return value
    

class Idvalidator(validators.RegexValidator):
    def __call__(self,value):
        if len(value) < 5:
            raise forms.ValidationError("El ID debe tener al menos 5 caracteres")
    
        if not value.isdigit():
            raise forms.ValidationError("El ID debe ser totalmente numerico")
            
        return value
    
class PhoneValidator(validators.RegexValidator):
    def __call__(self,value):
        if len(value) < 10:
            raise forms.ValidationError("Phone number must have at least 10 digits.")
        if not value.isdigit():
            raise forms.ValidationError("Debe contener solo valores numericos")
        
        return value 
            
            
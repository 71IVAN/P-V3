from django.db import models
from django.core.exceptions import ValidationError

def validate_name(value):
    if len(value) <= 3:
        raise ValidationError("Name must be at least 3 characters long")

def validate_phone(value):
    if len(value) != 10:
        raise ValidationError("Phone number must have 10 digits.")

def validate_address(value):
    if len(value) <= 10:
        raise ValidationError("Address must be at least 10 characters long")

def validate_identity_document(value):
    if len(value) < 5:
        raise ValidationError("Identity document must be at least 5 characters long")

def validate_email(value):
    allowed_domains = ['com', '.net', '.in', '.org']
    if not any(value.endswith(domain) for domain in allowed_domains):
        raise ValidationError("Email is not valid") 

class ModelThird(models.Model):
    type_Third = [
        ('clients', 'Clients'),
        ('Suppliers', 'Suppliers'),
        ('employees', 'Employees'),
        ('Financial Institutions', 'Financial Institutions')
    ]

    activo_choices = [
        ('1','SI'),
        ('0','NO'),
    ]

    name = models.CharField(max_length=100, verbose_name='name', validators=[validate_name]) 
    email = models.EmailField(verbose_name='email', validators=[validate_email])
    phone = models.CharField(max_length=17, verbose_name='phone', validators=[validate_phone])
    address = models.CharField(max_length=50, verbose_name='address', validators=[validate_address])
    typeThird = models.CharField(max_length=100, choices=type_Third, default='employees', verbose_name='typeThird')
    activo = models.CharField(max_length=2, choices=activo_choices, default='1', verbose_name='Activo')
    description = models.TextField(verbose_name='description', max_length=70)
    identity_document = models.CharField(verbose_name='identity_document', max_length=20, blank=False, validators=[validate_identity_document])
    hora = models.TimeField(verbose_name='Hora de registro', auto_now=True)

    class Meta:
        db_table = 'thirdF' 
        verbose_name = 'thirdsF'
        
    def __str__(self): 
        return self.name

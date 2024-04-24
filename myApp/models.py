from django.db import models
from django.core.validators import RegexValidator

class modeltest(models.Model):

    type_Third = [
        ('clients', 'Clients'),
        ('Suppliers', 'Suppliers'),
        ('employees', 'Employees'),
        ('Financial Institutions', 'Financial Institutions')     
    ]
    
    nombre = models.CharField(max_length=100,  null=False, blank=False, verbose_name='Name')
    email = models.EmailField(verbose_name='Email address', max_length=254, null=False, blank=False)
    telefono = models.CharField(max_length=17, verbose_name='telefono', validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$', 
    message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", code='invalid')], null=False, blank=False)
    
    address = models.CharField(max_length = 50, null=True, blank=False)
    typeThird = models.CharField(max_length = 100, blank=True, choices=type_Third, default=type_Third[3])
    activo = models.CharField(max_length=2, default='no')
    identity_document = models.CharField(max_length=20, blank=False)
    password = models.CharField(max_length=100, null=True, blank=False)

    class Meta:
        db_table = 'test'
        verbose_name = 'Test'

    def __str__(self):
        return self.nombre
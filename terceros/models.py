from django.db import models
from datetime import datetime

class ModelThird(models.Model):

    type_Third = [
        ('clients', 'Clients'),
        ('Suppliers', 'Suppliers'),
        ('employees', 'Employees'),
        ('Financial Institutions', 'Financial Institutions')
     
    ]

    activo_choises = [
        ('1','SI'),
        ('0','NO'),
    ]

    name = models.CharField(max_length = 100, verbose_name='Name and lastname') 
    email = models.EmailField(verbose_name = 'email')
    phone = models.CharField(max_length=17, verbose_name='phone')
    address = models.CharField(max_length = 50, verbose_name='Your Address')
    typeThird = models.CharField(max_length = 100, choices=type_Third, default='employees', verbose_name='Type Third')
    activo = models.CharField(max_length=2, choices=activo_choises, default='1', verbose_name='Activo')
    description = models.TextField(verbose_name = 'description', max_length=100)
    date_of_birth = models.DateField(default=datetime.now)
    identity_document = models.CharField(verbose_name='Identity Document', max_length=20, default='N/A')
    hora = models.TimeField(verbose_name='Hora de registro', auto_now=True)

    class Meta:
        db_table = 'thirdF' 
        verbose_name = 'thirdsF'
        
    def __str__(self):
        return self.name
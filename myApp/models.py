from django.db import models
from django.urls import reverse

# Create your models here.8D
class modeltest(models.Model):

    nombre = models.CharField(max_length=100,  null=False, blank=False, verbose_name='Name')
    email = models.EmailField(verbose_name='Email address', max_length=254, null=False, blank=False)
    telefono = models.CharField(max_length=17, verbose_name='phone')
    address = models.CharField(max_length = 50, null=True, blank=False)
    typeThird = models.CharField(max_length = 100, null=True, blank=False)
    activo = models.CharField(max_length=2, null=True, blank=False, default='si' )
    identity_document = models.CharField(max_length=20, default='N/A')

    class Meta:
        db_table = 'test'
        verbose_name = 'Test'

    def __str__(self):
        return self.nombre
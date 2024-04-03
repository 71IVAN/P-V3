from django.db import models
from django.core.exceptions import ValidationError

class modelBoostrap(models.Model):

    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100) 
    ide = models.CharField(max_length=10)
    phone = models.CharField(max_length=20)   
    description = models.TextField() 
    address = models.CharField(max_length=255)
    activo = models.CharField(max_length=10) 
    typethird = models.CharField(max_length=100) 
    class Meta:
        db_table = 'modelBoostrapApp'
        verbose_name = 'modelBoostrap_app'
        
    def __str__(self): 
        return self.name

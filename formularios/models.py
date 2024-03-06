from django.db import models

# Create your models here.
class third(models.Model):
    firstName = models.CharField(max_length=100, unique=True)
    lastName =  models.CharField(max_length=100, unique=True)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=254, unique=True)
    address = models.CharField(max_length=255)
    thirdPartyType = models.CharField(max_length=50)

    
    class Meta:
        db_table = 'third'
        verbose_name = 'thirds'
        
    def __str__(self):
        return self.firstName
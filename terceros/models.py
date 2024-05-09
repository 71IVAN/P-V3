from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from terceros.validators import UnicodeUserphonelValidator
# from validaciones.validators import EmailDomainValidator, Idvalidator, NameValidator, PhoneValidator

class ModelThird(models.Model):
    # validate_name = NameValidator()
    # validate_email = EmailDomainValidator()
    # validate_id = Idvalidator()
    # phoneRgex = RegexValidator(regex=r"^\d{10,15}$", message="Phone number must have 10 to 15 digits.") 
    # validate_fhone = PhoneValidator()
    
    name = models.CharField(max_length=50) 
    email = models.EmailField(unique=True) 
    phone = models.CharField(unique=True, max_length=12)
    identity_document = models.CharField(max_length=22)
    hora = models.TimeField(auto_now=True)

    class Meta:
        db_table = 'thirdF' 
        verbose_name = 'thirdsF'
        
    def __str__(self): 
        return self.name

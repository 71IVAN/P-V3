from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    cantidad = models.IntegerField()

    class Meta:
        db_table = "practica_db"
        verbose_name = "practica"
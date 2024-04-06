from django.db import models

# Create your models here.
class Tableone(models.Model):
    name = models.CharField(max_length=255, verbose_name="Name")
    description = models.TextField(verbose_name="Description", null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    def __str__(self):
        return self.name
# Generated by Django 4.2.9 on 2024-03-08 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0013_modeltest_identity_document'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modeltest',
            name='nombre',
            field=models.CharField(max_length=100, verbose_name='Nombre'),
        ),
    ]

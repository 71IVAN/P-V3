# Generated by Django 4.2.9 on 2024-03-04 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0006_modeltest_activo_modeltest_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modeltest',
            name='typeThird',
            field=models.CharField(choices=[('employees', 'employees'), ('customers', 'customers'), ('providers', 'providers'), ('Financial Institutions', 'Financial Institutions')], default='employees', max_length=100),
        ),
    ]

# Generated by Django 4.2.9 on 2024-04-01 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0022_alter_modeltest_activo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modeltest',
            name='typeThird',
            field=models.CharField(blank=True, choices=[('clients', 'Clients'), ('Suppliers', 'Suppliers'), ('employees', 'Employees'), ('Financial Institutions', 'Financial Institutions')], default=('clients', 'Clients'), max_length=100),
        ),
    ]

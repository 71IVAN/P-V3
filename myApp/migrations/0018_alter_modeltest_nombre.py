# Generated by Django 4.2.9 on 2024-03-18 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0017_alter_modeltest_telefono'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modeltest',
            name='nombre',
            field=models.CharField(max_length=100, verbose_name='Name'),
        ),
    ]
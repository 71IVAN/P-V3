# Generated by Django 4.2.9 on 2024-02-28 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0003_alter_modeltest_telefono'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modeltest',
            name='telefono',
            field=models.CharField(max_length=17, verbose_name='phone'),
        ),
    ]

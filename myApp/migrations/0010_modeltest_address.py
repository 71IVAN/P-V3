# Generated by Django 4.2.9 on 2024-03-04 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0009_remove_modeltest_activo_remove_modeltest_address_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='modeltest',
            name='address',
            field=models.CharField(max_length=50, null=True),
        ),
    ]

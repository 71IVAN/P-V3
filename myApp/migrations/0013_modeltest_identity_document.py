# Generated by Django 4.2.9 on 2024-03-04 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0012_modeltest_activo'),
    ]

    operations = [
        migrations.AddField(
            model_name='modeltest',
            name='identity_document',
            field=models.CharField(default='N/A', max_length=20),
        ),
    ]
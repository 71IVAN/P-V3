# Generated by Django 4.2.9 on 2024-03-04 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0010_modeltest_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='modeltest',
            name='typeThird',
            field=models.CharField(max_length=100, null=True),
        ),
    ]

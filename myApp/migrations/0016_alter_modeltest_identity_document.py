# Generated by Django 4.2.9 on 2024-03-13 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0015_alter_modeltest_typethird'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modeltest',
            name='identity_document',
            field=models.CharField(max_length=20),
        ),
    ]

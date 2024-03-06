# Generated by Django 4.2.9 on 2024-02-28 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='modeltest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, verbose_name='Email address')),
                ('telefono', models.IntegerField(max_length=20)),
            ],
            options={
                'verbose_name': 'Test',
                'db_table': 'test',
            },
        ),
    ]

# Generated by Django 4.1.3 on 2023-02-22 13:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_podaci_temperatura_u_c'),
    ]

    operations = [
        migrations.AlterField(
            model_name='podaci',
            name='Temperatura_u_C',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(-273.15)]),
        ),
    ]

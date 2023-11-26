# Generated by Django 4.2.6 on 2023-11-16 04:00

import catalogos.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogos', '0014_alter_animal_imagen_alter_animal_rfid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to=catalogos.models.imagen_rfid_path),
        ),
        migrations.AlterField(
            model_name='animal',
            name='rfid',
            field=models.CharField(max_length=13),
        ),
    ]

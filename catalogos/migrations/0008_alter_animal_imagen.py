# Generated by Django 4.2.6 on 2023-11-14 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogos', '0007_alter_animal_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='GanaderiaSoft/static/animales/'),
        ),
    ]

# Generated by Django 4.2.6 on 2023-11-15 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogos', '0010_alter_animal_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='raza',
            name='descripcion',
            field=models.TextField(null=True),
        ),
    ]

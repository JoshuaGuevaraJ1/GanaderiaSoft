# Generated by Django 4.2.6 on 2023-11-06 14:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rfid', models.CharField(max_length=13)),
                ('nombre', models.CharField(max_length=13, null=True)),
                ('fechaLlegada', models.DateTimeField(auto_now_add=True)),
                ('fechaSalida', models.DateTimeField(auto_now=True)),
                ('raza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogos.tipoanimal')),
            ],
        ),
    ]

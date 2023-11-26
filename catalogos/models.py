from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver

import os

# Create your models here.
class Grupo(models.Model):
    nombre = models.CharField(max_length=30, null=False)

    def __str__(self):
        return self.nombre

class Raza(models.Model):
    raza = models.CharField(max_length=50, null=False)
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)
    descripcion = models.TextField(null=True)

    def __str__(self):
        return "%s de raza %s" % (self.grupo, self.raza)
    
class Sexo(models.Model):
    sexo = models.CharField(max_length=7, null=False)

    def __str__(self):
        return self.sexo
    
def imagen_rfid_path(instance, filename):
    # Generar el nombre de archivo utilizando el RFID y la extensión original
    ext = filename.split('.')[-1]
    new_filename = f"{instance.rfid}.{ext}"
    # Devolver la ruta completa
    return os.path.join('GanaderiaSoft/static/img/animales/', new_filename)

class Animal(models.Model):
    rfid = models.CharField(max_length=13, null=False)
    nombre = models.CharField(max_length=13, null=True)
    raza = models.ForeignKey(Raza, on_delete=models.CASCADE)
    sexo = models.ForeignKey(Sexo, on_delete=models.CASCADE, null=True)
    fechaLlegada = models.DateField(auto_now_add=True)
    fechaSalida = models.DateField(null=True, blank=True)
    imagen = models.ImageField(upload_to=imagen_rfid_path, null=True, blank=True)

    def __str__(self):
        return "%s - %s - %s - %s - %s" % (self.rfid, self.nombre, self.raza, self.fechaLlegada, self.fechaSalidas)
    
def imagen_rfid_path(instance, filename):
    # Generar el nombre de archivo utilizando el RFID y la extensión original
    ext = filename.split('.')[-1]
    new_filename = f"{instance.rfid}.{ext}"

    # Devolver la ruta completa
    return os.path.join('GanaderiaSoft/static/img/animales/', new_filename)

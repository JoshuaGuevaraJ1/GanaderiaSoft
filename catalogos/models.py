from django.db import models

# Create your models here.
class TipoAnimal(models.Model):
    tipoAnimal = models.CharField(max_length=30, null=False)

    def __str__(self):
        return self.tipoAnimal

class Razas(models.Model):
    raza = models.CharField(max_length=50, null=False)
    tipoAnimal = models.ForeignKey(TipoAnimal, on_delete=models.CASCADE)

    def __str__(self):
        return "%s - %s" % (self.tipoAnimal, self.raza)
    
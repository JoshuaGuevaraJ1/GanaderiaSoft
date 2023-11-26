from django.contrib import admin

# Register your models here.
from catalogos.models import Grupo, Raza, Animal, Sexo
admin.site.register(Grupo)
admin.site.register(Raza)
admin.site.register(Animal)
admin.site.register(Sexo)
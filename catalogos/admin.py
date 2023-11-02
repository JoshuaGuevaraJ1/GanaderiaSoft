from django.contrib import admin

# Register your models here.
from catalogos.models import TipoAnimal, Razas
admin.site.register(TipoAnimal)
admin.site.register(Razas)
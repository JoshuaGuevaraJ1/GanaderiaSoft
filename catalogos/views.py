from django.shortcuts import render, redirect
from .models import TipoAnimal, Razas

# Create your views here.
def homeCatalogos(request):
    return render(request, 'homeCatalogos.html')

def tipoAnimal(request):
    razas = Razas.objects.all()
    data = {'razas' : razas}
    return render(request, "tipoAnimales.html", data)

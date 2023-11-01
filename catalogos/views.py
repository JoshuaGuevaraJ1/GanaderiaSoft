from django.shortcuts import render

# Create your views here.
def homeCatalogos(request):
    return render(request, 'homeCatalogos.html')

def tipoAnimal(request):
    return render(request, 'tipoAnimales.html')
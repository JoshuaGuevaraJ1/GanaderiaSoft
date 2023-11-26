"""
URL configuration for GanaderiaSoft project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from catalogos import views

urlpatterns = [
    path('homeCatalogos', views.homeCatalogos, name='homeCatalogos'),
    path('rfid', views.rfid, name='rfid'),

    path('razas/lista', views.razasList, name='razasList'),
    path('raza/agregar', views.razaCreate, name='razaCreate'),
    path('raza/editar/<int:pk>', views.razaUpdate, name='razaUpdate'),
    path('raza/eliminar/<int:pk>', views.razaDelete, name='razaDelete'),

    path('grupo/lista', views.grupoList, name='grupoList'),
    path('grupo/agregar', views.grupoCreate, name='grupoCreate'),
    path('grupo/editar/<int:pk>', views.grupoUpdate, name='grupoUpdate'),
    path('grupo/eliminar/<int:pk>', views.grupoDelete, name='grupoDelete'),
    
    path('animal/list', views.animalList, name='animalList'),
    path('animal/agregar', views.animalCreate, name='animalCreate'),
    path('animal/editar/<int:pk>', views.animalUpdate, name='animalUpdate'),
    path('animal/eliminar/<int:pk>', views.animalDelete, name='animalDelete'),

    path('buscar_ganado', views.buscar_ganado, name='buscar_ganado'),
    path('generarpdf/', views.generarpdf, name='generarpdf'),
    path('generar_informe_pdf/', views.generar_informe_pdf, name='generar_informe_pdf'),
]

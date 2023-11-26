from django.shortcuts import get_object_or_404, render, redirect, HttpResponse
from django.http import JsonResponse #Devolver arreglos de datos RFID
from django.utils import formats #Dar formatos a las fechas
from django.core.files.storage import FileSystemStorage #Para archivos y directorios
from django.contrib.auth.decorators import login_required #Forzar inicio de sesión

# PDF
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Image, Paragraph, BaseDocTemplate, Frame, PageTemplate, PageBreak
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfgen import canvas

import os
from .models import Grupo, Raza, Animal
from .forms import RazaForm, GrupoForm, AnimalForm, FiltroInformeForm

# Create your views here.
@login_required(login_url='signin')
def homeCatalogos(request):
    return render(request, 'homeCatalogos.html')

@login_required(login_url='signin')
def rfid(request):
    return render(request, 'rfid.html')

@login_required(login_url='signin')
def buscar_ganado(request):
    if request.method == 'GET':
        rfid = request.GET.get('rfid', '')
        try:
            animal = Animal.objects.select_related('raza__grupo').get(rfid=rfid)
            data = {
                'rfid': animal.rfid,
                'nombre': animal.nombre,
                'raza': f"{animal.raza.grupo} de raza {animal.raza.raza}",
                'fechaLlegada': formats.date_format(animal.fechaLlegada, "j F Y"),
                'fechaSalida': formats.date_format(animal.fechaSalida, "j F Y") if animal.fechaSalida else '',
                'imagenURL': animal.imagen.url if animal.imagen else ''
            }
            return JsonResponse(data)
        except Animal.DoesNotExist:
            return JsonResponse({'error': 'RFID no encontrado'})
    return JsonResponse({'error': 'Solicitud no válida'}, status=400)


# CRUD Raza
@login_required(login_url='signin')
def razasList(request):
    razas = Raza.objects.all()
    data = {'razas' : razas}
    return render(request, "razasList.html", data)

@login_required(login_url='signin')
def razaCreate(request):
    if request.method == 'POST':
        form = RazaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('razasList')
    else:
        form = RazaForm()
        return render(request, 'razaCreate.html', {'form' : form})

@login_required(login_url='signin')
def razaUpdate(request, pk):
    raza = get_object_or_404(Raza, pk=pk)
    if request.method == 'POST':
        form = RazaForm(request.POST, instance=raza)
        if form.is_valid():
            form.save()
            return redirect('razasList')
    else:
        form = RazaForm(instance=raza)
    return render(request, 'razaUpdate.html', {'form': form})

@login_required(login_url='signin')
def razaDelete(request, pk):
    raza = get_object_or_404(Raza, pk=pk)
    if request.method == 'POST':
        raza.delete()
        return redirect('razasList')
    return render(request, 'razaDelete.html', {'raza': raza})

#CRUD Tipo Animal
@login_required(login_url='signin')
def grupoList(request):
    grupos = Grupo.objects.all()
    data = {'grupos' : grupos}
    return render(request, "grupoList.html", data)

@login_required(login_url='signin')
def grupoCreate(request):
    if request.method == 'POST':
        form = GrupoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('grupoList')
    else:
        form = GrupoForm()
        return render(request, 'grupoCreate.html', {'form' : form})

@login_required(login_url='signin')
def grupoUpdate(request, pk):
    grupo = get_object_or_404(Grupo, pk=pk)
    if request.method == 'POST':
        form = GrupoForm(request.POST, instance=grupo)
        if form.is_valid():
            form.save()
            return redirect('grupoList')
    else:
        form = GrupoForm(instance=grupo)
    return render(request, 'grupoUpdate.html', {'form': form})

@login_required(login_url='signin')
def grupoDelete(request, pk):
    grupo = get_object_or_404(Grupo, pk=pk)
    if request.method == 'POST':
        grupo.delete()
        return redirect('grupoList')
    return render(request, 'grupoDelete.html', {'grupo': grupo})

# CRUD Animales
@login_required(login_url='signin')
def animalList(request):
    animales = Animal.objects.all()
    data = {'animales' : animales}
    return render(request, "animalList.html", data)

@login_required(login_url='signin')
def animalCreate(request):
    if request.method == 'POST':
        form = AnimalForm(request.POST, request.FILES)
        if form.is_valid():
            rfid = form.cleaned_data['rfid']

           # Verify if the RFID already exists
            if Animal.objects.filter(rfid=rfid).exists():
                error = 'Ya existe un Animal con este Rfid.'
                return render(request, 'animalCreate.html', {'form': form, 'error': error})

            
            form.save()
            return redirect('animalList')
        # Return a response even if the form is not valid
        else:
            return render(request, 'animalCreate.html', {'form': form})
    else:
        form = AnimalForm()
        return render(request, 'animalCreate.html', {'form' : form})

@login_required(login_url='signin')
def animalUpdate(request, pk):
    animal = get_object_or_404(Animal, pk=pk)
    if request.method == 'POST':
        form = AnimalForm(request.POST, request.FILES, instance=animal)
        if form.is_valid():
            # Procesar la imagen
            imagen = request.FILES['imagen'] if 'imagen' in request.FILES else None

            # Si el animal no tiene imagen
            if not animal.imagen:
                # Sobrescribir la imagen existente
                animal.imagen = imagen
            else:
                imagenActual = animal.imagen
                if imagen:
                    # Eliminar la imagen existente
                    fs = FileSystemStorage()
                    fs.delete(animal.imagen.name)
                    # Sobrescribir la imagen existente
                    animal.imagen = imagen
                else:
                    animal.imagen = imagenActual

            form.save()
            return redirect('animalList')
    else:
        form = AnimalForm(instance=animal)
    return render(request, 'animalUpdate.html', {'animal': animal,'form': form})

@login_required(login_url='signin')
def animalDelete(request, pk):
    animal = get_object_or_404(Animal, pk=pk)
    if request.method == 'POST':
        # Eliminar la imagen
        if animal.imagen:
            fs = FileSystemStorage()
            fs.delete(animal.imagen.name)
        animal.delete()
        return redirect('animalList')
    return render(request, 'animalDelete.html', {'grupo': animal})



@login_required(login_url='signin')
def generar_informe_pdf(request):
    form = FiltroInformeForm(request.GET)

    if form.is_valid():
        datos_filtrados = Animal.objects.all()

        grupo = form.cleaned_data['grupo']
        if grupo:
            datos_filtrados = datos_filtrados.filter(raza__grupo__nombre=grupo)

        sexo = form.cleaned_data['sexo']
        if sexo:
            datos_filtrados = datos_filtrados.filter(sexo__sexo=sexo)

        fecha_llegada_inicio = form.cleaned_data['fecha_llegada_inicio']
        fecha_llegada_fin = form.cleaned_data['fecha_llegada_fin']
        if fecha_llegada_inicio:
            datos_filtrados = datos_filtrados.filter(fechaLlegada__gte=fecha_llegada_inicio)
        if fecha_llegada_fin:
            datos_filtrados = datos_filtrados.filter(fechaLlegada__lte=fecha_llegada_fin)

        fecha_salida_inicio = form.cleaned_data['fecha_salida_inicio']
        fecha_salida_fin = form.cleaned_data['fecha_salida_fin']
        if fecha_salida_inicio:
            datos_filtrados = datos_filtrados.filter(
                fechaSalida__gte=fecha_salida_inicio,
                fechaSalida__isnull=False  # Excluir animales sin fecha de salida
            )
        if fecha_salida_fin:
            datos_filtrados = datos_filtrados.filter(
                fechaSalida__lte=fecha_salida_fin,
                fechaSalida__isnull=False  # Excluir animales sin fecha de salida
            )
    else:
        datos_filtrados = Animal.objects.all()

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="informe.pdf"'

    # Crear el objeto PDF usando reportlab
    doc = SimpleDocTemplate(response, pagesize=letter, leftMargin=20, rightMargin=20, topMargin=20, bottomMargin=20)
    elements = []

    # Definir estilos para el título
    styles = getSampleStyleSheet()
    estilo_titulo = styles['Heading1']

    # Agregar título al PDF
    titulo = Paragraph('<font size=14>Ganadería Soft 2.0 (Reporte PDF)</font>', estilo_titulo)
    elements.append(titulo)

    # Agregar datos filtrados al PDF en forma de tabla
    data = [['Imagen', 'RFID', 'Nombre', 'Raza', 'Sexo', 'Fecha Llegada', 'Fecha Salida']]

    for dato in datos_filtrados:
        row = [
            Image(dato.imagen.path, width=1*inch, height=1*inch) if dato.imagen else "",  # Miniatura de la imagen
            dato.rfid,
            dato.nombre,
            str(dato.raza),
            dato.sexo.sexo if dato.sexo else "N/A",
            dato.fechaLlegada.strftime('%Y-%m-%d'),
            dato.fechaSalida.strftime('%Y-%m-%d') if dato.fechaSalida else "N/A"
        ]
        data.append(row)

    # Crear la tabla
    table = Table(data)
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),  # Centrar todo el texto verticalmente
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
    ])
    # Agregar encabezado a la tabla
    table = Table(data, style=style)
    # table.setStyle(style)
    
    # Agregar tabla al PDF
    elements.append(table)

    # Agregar PageBreak para iniciar una nueva página
    elements.append(PageBreak())

    # Construir el PDF
    # doc.build(elements)
    doc.build(elements, onFirstPage=add_page_number, onLaterPages=add_page_number)


    return response

def add_page_number(canvas, doc):
    # Agregar número de página al pie de página
    page_num = canvas.getPageNumber()
    text = "Página %s" % (page_num)
    canvas.drawRightString(200*doc.width/300, 20, text)

@login_required(login_url='signin')
def generarpdf(request):
    form = FiltroInformeForm()
    return render(request, 'generarpdf.html', {'form': form})
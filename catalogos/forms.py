from django import forms
from .models import Raza, Grupo, Animal, Sexo

class RazaForm(forms.ModelForm):
    class Meta:
        model = Raza
        fields = '__all__'
        
    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class' : 'form-control'})
    

class GrupoForm(forms.ModelForm):
    class Meta:
        model = Grupo
        fields = '__all__'
        
    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class' : 'form-control'})

class AnimalForm(forms.ModelForm):
    fechaSalida = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}), required=False,label='Fecha de Salida (solo si ya salió del ganado)')

    class Meta:
        model = Animal
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class': 'form-control'})
        self.fields['imagen'].widget.attrs.update({'class': 'btn btn-info btn-icon-split'})


class FiltroInformeForm(forms.Form):
    grupo_choices = [('','---')] + [(grupo.nombre, grupo.nombre) for grupo in Grupo.objects.all()]
    sexo_choices = [('','---')] + [(sexo.sexo, sexo.sexo) for sexo in Sexo.objects.all()]

    

    grupo = forms.ChoiceField(choices=grupo_choices, required=False)
    sexo = forms.ChoiceField(choices=sexo_choices, required=False)
    fecha_llegada_inicio = forms.DateTimeField(widget=forms.TextInput(attrs={'type': 'date'}), required=False)
    fecha_llegada_fin = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}), required=False)
    fecha_salida_inicio = forms.DateTimeField(widget=forms.TextInput(attrs={'type': 'date'}), required=False)
    fecha_salida_fin = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}), required=False)

    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class' : 'form-control'})
from django import forms 
from .models import Peticion
import datetime

class PeticionForm(forms.ModelForm):
    class Meta:
        model = Peticion
        fields= '__all__'

def clean_fecha_inicial(self):
    #validación de fecha solicitud
    fecha_inicial=self.cleaned_data.get('fecha_inicial')
    fecha_solicitud=self.cleaned_data.get('fecha_solicitud')
     
    if fecha_inicial > fecha_solicitud:
        raise forms.ValidationError('La fecha inicial de atención no puede ser superior a la fecha de solicitud.') 
    return fecha_inicial

    

def clean_fecha_final(self):
    #validación de fecha solicitud
    fecha_final=self.cleaned_data.get('fecha_final')
    fecha_solicitud=self.cleaned_data.get('fecha_solicitud')
     
    if fecha_final>fecha_solicitud:
        raise forms.ValidationError('La fecha final de atención no puede ser superior a la fecha de solicitud.')
    return fecha_final
    
from django import forms 
from .models import Peticion
from datetime import datetime
from django.core.exceptions import ValidationError

class PeticionForm(forms.ModelForm):
    class Meta:
        model = Peticion
        fields= '__all__'

    ''' ------------- EN EL CODIGO QUE ESTÁ ABAJO SE REALIZA LA VALIDACIÓN DE LAS FECHAS -----------------------
        ------------- LO PONGO COMO UN COMENTARIO DEBIDO A QUE MI TERMINAL DE PYTHON    -----------------------
        ------------- NO PUDO IMPORTAR DATETIME DE LA LIBRERIA DATETIME   -------------------------------------
        ------------- POR LO TANTO NO ME PERMITE EJECUTAR LAS VALIDACIONES--------------------------------------
                       
    def clean_fecha_inicial(self):
        #validación de fecha solicitud
        fecha_inicial=self.cleaned_data.get('fecha_inicial')
        fecha_solicitud=self.cleaned_data.get('fecha_solicitud')
        if fecha_inicial>fecha_solicitud:
            raise forms.ValidationError('La fecha inicial de atención no puede ser superior a la fecha de solicitud.') 
        return fecha_inicial
    
    def clean_fecha_final(self):
        #validación de fecha solicitud
        fecha_final=self.cleaned_data.get('fecha_final')
        fecha_solicitud=self.cleaned_data.get('fecha_solicitud')
        if fecha_final>fecha_solicitud:
            raise forms.ValidationError('La fecha final de atención no puede ser superior a la fecha de solicitud.') 
        return fecha_final'''
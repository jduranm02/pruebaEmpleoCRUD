from django import forms 
from .models import Peticion
import datetime

class PeticionForm(forms.ModelForm):
    class Meta:
        model = Peticion
        fields= '__all__'

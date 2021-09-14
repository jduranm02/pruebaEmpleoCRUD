from django import forms 
from .models import Peticion

class PeticionForm(forms.ModelForm):
    class Meta:
        model = Peticion
        fields= '__all__'
from django.shortcuts import render
from .models import Peticion

def inicio(request):
    peticiones=Peticion.objects.all()
    contexto={
        'peticiones':peticiones
    }
    print(peticiones)
    return render(request,'index.html',contexto)
from django.shortcuts import redirect, render
from .models import Peticion
from .forms import PeticionForm

def inicio(request):
    peticiones=Peticion.objects.all()
    contexto={
        'peticiones':peticiones
    }
    print(peticiones)
    return render(request,'index.html',contexto)

def crearPeticion(request):
    if request.method == 'GET':
        form = PeticionForm()
        contexto={
            'form':form
        }
    else:
        form=PeticionForm(request.POST)
        contexto={
            'form':form
        }
        print(form)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request,'crearPeticion.html',contexto)

def editarPeticion(request,id):
    peticion= Peticion.objects.get(id = id)
    if request.method == 'GET':
        form=PeticionForm(instance=peticion)
        contexto={
            'form':form
        }
    else:
        form=PeticionForm(request.POST,instance=peticion)
        contexto={
            'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request,'crearPeticion.html',contexto)
    
def eliminarPeticion(request,id):
    peticion=Peticion.objects.get(id = id)
    peticion.delete()
    return redirect ('index')

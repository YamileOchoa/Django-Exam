from django.shortcuts import render, redirect, get_object_or_404
from .models import Eventos
from .forms import EventosForm  ##
# Create your views here.

def listar_eventos(request):
    eventos = Eventos.objects.all()
    return render(request, 'eventos/lista.html', {'eventos': eventos})

def crear_evento(request):
    if request.method == 'POST':
        form = EventosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_eventos')
    else:
        form = EventosForm()
    return render(request, 'eventos/form.html', {'form': form})

def editar_eventos(request, id):
    if request.method == 'POST':
        form = EventosForm(request.POST, id=id)
        if form.is_valid():
            form.save()
            return redirect('listar_eventos')
    else:
        form = EventosForm(instance=form)
    return render(request, 'eventos/form.html', {'form': form})
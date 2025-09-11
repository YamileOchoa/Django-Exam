from django.shortcuts import render, redirect, get_object_or_404
from .models import Organizadores
from .forms import OrganizadoresForm    
# Create your views here.

def listar_organizadores(request):
    organizardores = Organizadores.objects.all()
    return render(request, 'organizadores/lista.html', {'organizadores': organizardores})

def crear_organizador(request):
    if request.method == 'POST':
        form = OrganizadoresForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_organizadores')
    else:
        form = OrganizadoresForm()
    return render(request, 'organizadores/form.html', {'form': form})

def editar_organizador(request, id):
    if request.method == 'POST':
        form = OrganizadoresForm(request.POST, id=id)
        if form.is_valid():
            form.save()
            return redirect('listar_organizadores')
    else:
        form = OrganizadoresForm(instance=form)
    return render(request, 'organizadores/form.html', {'form': form})

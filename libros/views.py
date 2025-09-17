from django.shortcuts import render, redirect, get_object_or_404
from .models import Libro
from .forms import LibroForm

# Create your views here.
def libro_list(request):
    libros = Libro.objects.all()
    return render(request, 'libros/libro_list.html', {'libros': libros})

def libro_create(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("libros:libro_list")
    else:
        form = LibroForm()
    return render(request, 'libros/libro_form.html', {'form': form})

def libro_edit(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    if request.method == 'POST':
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            return redirect("libros:libro_list")
    else:
        form = LibroForm(instance=libro)
    return render(request, 'libros/libro_form.html', {'form' : form})

def libro_delete(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    if request.method == 'POST':
        libro.delete()
        return redirect('libros:libro_list')
    return render(request, 'libros/libro_confirm_delete.html', {'libro' : libro})
from django.shortcuts import render, redirect, get_object_or_404
from .models import Estudiante
from estudiante.froms import EstudianteForms

# LISTAR
def listarEstudiante(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'estudiantes/lista.html', {
        'estudiantes': estudiantes
    })

# CREAR
def crearEstudiante(request):
    if request.method == 'POST':
        form = EstudianteForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_estudiante')
    else:
        form = EstudianteForms()

    return render(request, 'estudiantes/form.html', {
        'form': form
    })

# EDITAR
def editarEstudiante(request, id):
    estudiante = get_object_or_404(Estudiante, id=id)

    if request.method == 'POST':
        form = EstudianteForms(request.POST, instance=estudiante)
        if form.is_valid():
            form.save()
            return redirect('lista_estudiante')
    else:
        form = EstudianteForms(instance=estudiante)

    return render(request, 'estudiantes/form.html', {
        'form': form
    })

# ELIMINAR
def eliminarEstudiante(request, id):
    estudiante = get_object_or_404(Estudiante, id=id)

    if request.method == 'POST':
        estudiante.delete()
        return redirect('lista_estudiante')

    return render(request, 'estudiantes/eliminado.html', {
        'estudiante': estudiante
    })

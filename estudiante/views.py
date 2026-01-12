from django.shortcuts import render, redirect, get_object_or_404
from estudiante.models import Estudiante
from estudiante.froms import EstudianteForms

# CRUD ESTUDIANTES

## Crear Estudiante
def crearEstudiante(request):
    if request.method == 'POST':
        form = EstudianteForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_estudiante')
    else:
        form = EstudianteForms()

    return render(request, 'estudiantes/form.html', {
        'form': form
    })

## Listar Estudiante

def listarEstudiante(request):
    estudiantes = Estudiante.objects.all()
    return render(request, "estudiantes/lista.html", {"estudiantes":estudiantes})

## Editar Estudiantes

def editarEstudiantes(request, id):
    estudiante = get_object_or_404(Estudiante, id=id)
    if request.method == 'POST':
        estudianteform = EstudianteForms(request.POST, instance=estudiante)
        estudianteform.is_valid()
        estudianteform.save()
        return redirect("lista_estudiantes")
    else:
        estudianteform = EstudianteForms(instance=estudiante)

    return render(request, "estudiantes/form.html", {"estudianteforms": estudianteform})

## Eliminar Estudiantes

def eliminarEstudiante(request, id):
    estudiante = get_object_or_404(Estudiante, id=id)
    if request.method == 'POST':
        estudiante.delete()
        return redirect("lista_estudiantes")
    return render(request, "estudiantes/eliminado.html", {"estudiante": estudiante})
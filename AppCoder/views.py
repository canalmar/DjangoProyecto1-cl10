from django.shortcuts import render, get_object_or_404
from .models import Estudiante, Profesor, Curso, Entregable


# Create your views here.

def lista_estudiantes(request):
    lista_estudiantes = Estudiante.objects.all()
    return render (request, 'AppCoder/estudiantes_list.html', {'estudiantes': lista_estudiantes})

def detalle_estudiante(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    return render(request, 'AppCoder/estudiante_detail.html', {'estudiante':estudiante})

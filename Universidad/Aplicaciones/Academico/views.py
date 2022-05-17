from django.shortcuts import redirect, render
from .models import Curso
from django.contrib import messages

# Create your views here.

def inicio(request):
    return render(request, "index.html")

def contacto(request):
    return render(request, "contacto.html")

def home(request):
    cursosListados = Curso.objects.all()
    return render(request, "gestionCursos.html", {"cursos": cursosListados})

def registrarCurso(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    precio = request.POST['numPrecio']

    curso = Curso.objects.create(
        codigo=codigo, nombre=nombre, precio=precio
    )
    messages.success(request, 'Curso registrado')
    return redirect('/cursos')

def edicionCurso(request, codigo):
    curso = Curso.objects.get(codigo=codigo)
    return render(request, "edicionCurso.html", {"curso": curso})

def editarCurso(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    precio = request.POST['numPrecio']

    curso = Curso.objects.get(codigo=codigo)
    curso.nombre = nombre
    curso.precio = precio
    curso.save()

    messages.success(request, 'Curso actualizado')

    return redirect('/cursos')

def eliminarCurso(request,codigo):
    curso = Curso.objects.get(codigo=codigo)
    curso.delete()

    messages.success(request, 'Se ha eliminado el curso')

    return redirect('/cursos')
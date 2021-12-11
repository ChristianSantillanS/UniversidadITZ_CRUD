from django.shortcuts import redirect, render
from .models import Alumnos
from django.contrib import messages
# Create your views here.

def home(request):
    Alumno = Alumnos.objects.all()
    return render(request,"GestionCursos.html",{"alumnos":Alumno})

def agregar_a(request):
    
    return render(request, "agregar_a.html")

def registraralumnos(request):
    No_control = request.POST['txtNo_control']
    Apellido_p = request.POST['txtApellido_p']
    Apellido_m = request.POST['txtApellido_m']
    Nombres = request.POST['txtNombres']
    correo = request.POST['txtcorreo']
    alumnos = Alumnos.objects.create(
    No_control= No_control, Apellido_p = Apellido_p, Apellido_m = Apellido_m, Nombres = Nombres, correo = correo
    )
    messages.success(request,'¡Alumno agregado!')
    return redirect('/')
def eliminacionA(request, No_control):
    alumnos = Alumnos.objects.get(No_control=No_control)
    alumnos.delete()
    return redirect('/')
def edicionA(request,No_control):
    alumnos = Alumnos.objects.get(No_control=No_control)
    return render(request,"edicionA.html",{"alumnos":alumnos})

def editaralumnos(request):
    No_control = request.POST['txtNo_control']
    Apellido_p = request.POST['txtApellido_p']
    Apellido_m = request.POST['txtApellido_m']
    Nombres = request.POST['txtNombres']
    correo = request.POST['txtcorreo']
    alumnos = Alumnos.objects.get(No_control=No_control)
    alumnos.Apellido_p = Apellido_p
    alumnos.Apellido_m = Apellido_m
    alumnos.Nombres = Nombres
    alumnos.correo = correo
    alumnos.save()
    return redirect('/')
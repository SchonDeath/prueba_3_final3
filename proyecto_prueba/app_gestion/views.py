from django.shortcuts import render

# Create your views here.

from app_gestion.models import personas
from django.http import HttpResponse

def ingresar_persona(request):
    return render(request,"ingresar_persona.html")

def index(request):
    return render(request,"index.html")

def buscar_persona(request):
    return render(request,"buscar_persona.html") 

def listar_pacientes(request):
    return render(request,"listar_pacientes.html")


def eliminar_persona(request):
    return render(request,"eliminar_persona.html")


# Create your views here.


 


def ingreso_persona(request):
    rut=request.GET["txt_rut"]
    nombre=request.GET["txt_nombre"]
    apellido_paterno=request.GET["txt_apellido_paterno"]
    apellido_materno=request.GET["txt_apellido_materno"]
    edad=request.GET["txt_edad"]
    nombre_vacuna=request.GET["txt_nombre_vacuna"]
    fecha=request.GET["txt_fecha"]
    if len(rut)>0 and len(nombre)>0 and len(apellido_paterno)>0 and len(apellido_materno)>0 and len(edad)>0 and len(nombre_vacuna)>0 and len(fecha)>0:
        pro=personas(rut=rut,nombre=nombre,apellido_parterno=apellido_paterno,apellido_materno=apellido_materno,edad=edad,nombreVacuna=nombre_vacuna,fecha=fecha)  
        pro.save()
        mensaje="Persona ingresada correctamente..."
    else:
        mensaje="Persona no ingresada, faltan datos..."
    return render(request, "ingresar_persona.html", {'mensaje':mensaje})


def listar_personas(request):
    datos = personas.objects.all()  
    return render(request,"listar_pacientes.html",{'personas':datos})



def buscador(request):
    if request.GET["txt_rut"]:
        pers = request.GET["txt_rut"]
        persons = personas.objects.filter(rut__icontains=pers)
        return render(request,"listar.html",{"personas":persons,"query":pers})
    else:
        mensaje = "Debe ingresar un rut correspondiente"
        return render(request, "buscar_paciente.html", {'mensaje':mensaje})


def eliminar_persona_rut(request):
    if request.GET["txt_rut"]:
        rut_ingresado = request.GET["txt_rut"]
        persona = personas.objects.filter(rut=rut_ingresado)
        if persona:
            per=personas.objects.get(rut=rut_ingresado)
            per.delete()
            mensaje = "Persona elimina correctamente..."
        else:
            mensaje = "Rut no valido, la persona no esta registrada."
    else:
        mensaje = "Debe ingresar un rut  para eliminación..."
    return render(request, "eliminar_persona.html", {'mensaje':mensaje})
 
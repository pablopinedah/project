from django.shortcuts import render, redirect
from . import forms
from . import models 
from django.urls import reverse
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from decimal import Decimal


# Create your views here.
def index(request):
    return render(request, 'home/index.html')

#! Se crea la función crear_cliente para ingresar por el usuario los datos de la empresa.
def crear_cliente(request):
    if request.method == "POST":
        form = forms.ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home:index")
    else:
            form = forms.ClienteForm()
            context = {"form": form}
    return render(request, "home/crear_cliente.html",context)

#! Se crea la función crear_alcance1 para ingresar por el usuario los datos de las emisiones de alcance1
def crear_alcance1(request):
    if request.method == "POST":
        form = forms.Alcance1Form(request.POST)
        if form.is_valid():
            alcance1 = form.save()
            calculo_emision_refrigerante(request, alcance1)
            return redirect('home:mostrar_resultados')
    else:
        form = forms.Alcance1Form()
    
    context = {"form": form}
    return render(request, "home/crear_alcance1.html", context)
    
#! Se crea la función crear_alcance2 para ingresar por el usuario los datos de las emisiones de alcance2
def crear_alcance2(request):
    if request.method == "POST":
        form = forms.Alcance2Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home:index")
    else:
            form = forms.Alcance2Form()
            context = {"form": form}
    return render(request, "home/crear_alcance2.html",context)

#! Se crea la función para el Cálculo emisiones alcance1:
def calculo_emision_refrigerante(request, alcance1):
    refrigerante = alcance1.refrigerante
    cantidad_refrigerante_kg = alcance1.cantidad_refrigerante_kg
    
    factor = models.Factor_emision_gas_refrigerante.objects.all().values("GWP").filter(TIPO_REFRIGERANTE=refrigerante)
    if factor:
        gwp = factor[0].get("GWP")
        resultado_emision_gas_refrigerante = float(cantidad_refrigerante_kg) * gwp
        print(resultado_emision_gas_refrigerante)
        models.ResultadoEmisionGasRefrigerante.objects.create(valor=resultado_emision_gas_refrigerante).save()

#!  Se crea la función mostrar_resultado para las emisiones del alcance1 por Refrigerante:
def mostrar_resultados(request):
    factor_emision = models.ResultadoEmisionGasRefrigerante.objects.all()
    return render(request, 'home/calculo_emision_refrigerante.html', {'factor_emision': factor_emision})









#********************************
#! Creamos la función about
def about(request):
    return render(request, 'home/about.html')    

#! Creamos la función para el login
def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            contraseña = form.cleaned_data.get('password')
            user = authenticate(username= usuario, password=contraseña)
            if user is not None:
                login(request, user)
                return render(request, "home/index.html", {"mensaje":f"Bienvenido {usuario}"})
    else:
        form = AuthenticationForm()
    return render(request, "home/login.html", {"form": form})

#! El registro de una nueva empresa:
def register(request):
    if request.method == "POST":
        form = forms.CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "home/index.html", {"messages": "Empresa creada"})
    else:
        form = forms.CustomUserCreationForm()
    return render(request, "home/register.html", {"form": form})

   







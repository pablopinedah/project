from django.shortcuts import render, redirect
from . import forms
from . import models 
from django.urls import reverse
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate



# Create your views here.
def index(request):
    return render(request, 'home/index.html')

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
    
#
def crear_alcance1(request):
    if request.method == "POST":
        form = forms.Alcance1Form (request.POST)
        if form.is_valid():
            form.save()
            refrigerante = request.POST.get('refrigerante')
            cantidad_refrigerante_kg = request.POST.get('cantidad_refrigerante_kg')
            factor = models.Factor_emision_gas_refrigerante.objects.get(TIPO_REFRIGERANTE=refrigerante)
            gwp = factor.GWP
            emision_refrigerante = cantidad_refrigerante_kg * gwp
            return redirect('calculo-emision-refrigerante', emision_refrigerante=emision_refrigerante)
    else:
        form = forms.Alcance1Form()
        context = {"form": form}
    return render(request, "home/crear_alcance1.html",context)
#

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


#!  Cálculo emisiones alcance1:
#esta manera parece resultar poco eficiente, se prueba otra manera (abajo)
#def calculo_emision_refrigerante(request):
#    if request.method == 'POST':
#        refrigerante = request.POST.get('refrigerante')
#        cantidad_refrigerante_kg = request.POST.get('cantidad_refrigerante_kg')
#        factor = models.Factor_emision_gas_refrigerante.objects.get(TIPO_REFRIGERANTE=refrigerante)
#        gwp = factor.GWP
#        emision_refrigerante = cantidad_refrigerante_kg * gwp
        
#        return render(request, "home/calculo_emision_refrigerante.html", {'emision_refrigerante': emision_refrigerante})
#    else:
#        return render(request, "home/crear_alcance1.html")    


#Probando otra manera:
def crear_alcance1(request):
    form = forms.RefrigeranteForm()

    if request.method == 'POST':
        form = forms.RefrigeranteForm(request.POST)
        if form.is_valid():
            form.save()
            refrigerante = request.POST.get('refrigerante')
            cantidad_refrigerante_kg = request.POST.get('cantidad_refrigerante_kg')
            factor = models.Factor_emision_gas_refrigerante.objects.get(TIPO_REFRIGERANTE=refrigerante)
            gwp = factor.GWP
            emision_refrigerante = cantidad_refrigerante_kg * gwp
                        
            return redirect('nombre_de_la_vista')  # Redirecciona a una vista de tu elección

    context = {'form': form}
    return render(request, 'mi_plantilla.html', context)


def crear_alcance1(request):
    if request.method == "POST":
        form = forms.Alcance1Form (request.POST)
        if form.is_valid():
            form.save()
            refrigerante = request.POST.get('refrigerante')
            cantidad_refrigerante_kg = request.POST.get('cantidad_refrigerante_kg')
            factor = models.Factor_emision_gas_refrigerante.objects.get(TIPO_REFRIGERANTE=refrigerante)
            gwp = factor.GWP
            emision_refrigerante = cantidad_refrigerante_kg * gwp
            return redirect('calculo-emision-refrigerante', emision_refrigerante=emision_refrigerante)
    else:
        form = forms.Alcance1Form()
        context = {"form": form}
    return render(request, "home/crear_alcance1.html",context)
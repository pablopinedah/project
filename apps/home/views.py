from django.shortcuts import render, redirect
from . import forms
from . import models 
from django.urls import reverse
from django.http import HttpRequest, HttpResponse


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
    
def crear_alcance1(request):
    if request.method == "POST":
        form = forms.Alcance1Form (request.POST)
        if form.is_valid():
            form.save()
            return redirect("home:index")
    else:
            form = forms.Alcance1Form()
            context = {"form": form}
    return render(request, "home/crear_alcance1.html",context)

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


#Vamos a mostrar los resultado del cálculo de la huella de carbono:
def calculo_emision_refrigerante(request):
    factor_emision = models.Factor_emision_gas_refrigerante.objects.all()
    context = {"factor_emision": factor_emision}
    return render(request, "home/calculo-emision-refrigerante.html", context)
    
    #valor_refrigerante = float(request.POST.get())
    

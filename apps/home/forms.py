from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

from . import models

#Se crean tres formularios:
class ClienteForm(forms.ModelForm):
    class Meta:
        model =models.Cliente
        fields = "__all__"

class Alcance1Form(forms.ModelForm):
    class Meta:
        model =models.Alcance1
        fields = "__all__"
        
class Alcance2Form(forms.ModelForm):
    class Meta:
        model =models.Alcance2
        fields = "__all__"

#Se crea un formulario para las constantes:
class Factor_emision_gas_refrigeranteForm(forms.ModelForm):
    class Meta:
        model = models.Factor_emision_gas_refrigerante
        fields = "__all__"
        # ['refrigerante']





#se crea registro:
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username","email", "password1", "password2"]
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.TextInput(attrs={"class": "form-control"}),
            "password1": forms.PasswordInput(attrs={"class": "form-control"}),
            "password2": forms.PasswordInput(attrs={"class": "form-control"}),
        }
        help_texts = {k: "" for k in fields}


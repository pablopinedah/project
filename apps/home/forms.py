from django import forms

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


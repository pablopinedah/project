from django.db import models

# Se crea un modelo para poder guardas datos en el formulario.

#Se crear la clase Cliente para solicar los datos de la empresa: 
class Cliente(models.Model):
    empresa = models.CharField(max_length=20)
    pais = models.CharField(max_length=20, default='')
    numero_empleados = models.IntegerField(default=1, null=True, blank=True)
    año_datos = models.IntegerField(default=2020, null=True, blank=True)
    
    
    
    def __str__(self):
        return self.empresa 
 
 #Se crea la clase Alcance1 para solicitar los datos de emisiones directas por Equipos de Aire Acondicionado:
class Alcance1(models.Model):
    refrigerante = models.CharField(max_length=20)
    cantidad_refrigerante = models.FloatField()
    
    def __str__(self):
        return self.refrigerante  
    
#Se crea la clase Alcance2 para solitar los datos de emisiones directas por el consumo de electricidad
class Alcance2(models.Model):
    consumo_energia_electrica = models.FloatField()
    mes = models.CharField(max_length=20)
    
    def __str__(self):
        return str(self.consumo_energia_electrica)  

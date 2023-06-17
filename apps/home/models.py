from django.db import models
from django.contrib import admin


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
    cantidad_refrigerante_kg = models.FloatField()
    
    def __str__(self):
        return self.refrigerante  
    
#Se crea la clase Alcance2 para solitar los datos de emisiones directas por el consumo de electricidad
class Alcance2(models.Model):
    consumo_energia_electrica_kwh = models.FloatField()
    mes = models.CharField(max_length=20)
    
    def __str__(self):
        return str(self.consumo_energia_electrica_kwh)  
    
#! CONSTANTES, FACTORES DE EMISIÓN (CANTIDAD/CO2):
#Se crea un modelo para los factores de emisión, son constante que cambia anualmente, esto se hace por el panel de administración

class Factor_emision_gas_refrigerante(models.Model):
    
    TIPO_REFRIGERANTE = models.CharField(max_length=20) #el TIPO_REFRIGERANTE puede ser: R-410A, entre otros
    GWP = models.DecimalField(max_digits=6, decimal_places=2) #ejemplo R-410A tiene un GWP=1924.00, es el valor numérico
    
    class Meta:
        # db_table = ''
        # managed = True
        verbose_name = 'Tipo de Refrigerante (AR5)'
        verbose_name_plural = 'Tipos de Refrigerantes (AR5)'
    def __str__(self):
        return self.TIPO_REFRIGERANTE


class Factor_emision_consumo_energiaelectrica(models.Model):    
    PAIS = models.CharField(max_length=20, default='')
    AÑO_FACTOR_EMISION = models.IntegerField(default=2020, null=True, blank=True)  
    FACTOR_EMISION_ELECTRICIDAD = models.DecimalField(max_digits=4, decimal_places=3) #ejemplo factor de emisión en colombia en el 2020 0.203
    
    class Meta:
        # db_table = ''
        # managed = True
        ordering = ['AÑO_FACTOR_EMISION']
        verbose_name = 'Factor de emisión por consumo de energía (kg CO2e/kWh)'
        verbose_name_plural = 'Factores de emisión por consumo de energía (kg CO2e/kWh)'
    
    def __str__(self):
        return self.PAIS   

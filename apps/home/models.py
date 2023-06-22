from django.db import models
from django.contrib import admin



# Se crea un modelo para poder guardas datos en el formulario, datos a ingresar por el usuario:
#! Se crear la clase Cliente para solicitar los datos de la empresa al usuario. 
class Cliente(models.Model):
    empresa = models.CharField(max_length=20)
    pais = models.CharField(max_length=20, default='')
    numero_empleados = models.IntegerField(default=1, null=True, blank=True)
    año_datos = models.IntegerField(default=2020, null=True, blank=True)  
    
    def _str_(self):
        return self.empresa

#! Se crea la clase Alcance1 para solicitar al usuario los datos de emisiones directas por Equipos de Aire Acondicionado:
class Alcance1(models.Model):
    refrigerante = models.CharField(max_length=20) #corresponde al tipo de refrigerante, ejemplo R22. Lo ingresa el usuario.
    cantidad_refrigerante_kg = models.FloatField() #corresponde a la cantidad de refrigerante. Lo ingresa el usuario.

    def _str_(self):
        return self.refrigerante

#! Se crea la clase Alcance2 para solicitar al usuario los datos de emisiones directas por el consumo de electricidad
class Alcance2(models.Model):
    consumo_energia_electrica_kwh = models.FloatField() #es el valor de consumo de kwh. Lo ingresa el usuario.
    año = models.FloatField() #es el mes del consumo de energía. Lo ingresa el usuario.

    def _str_(self):
        return str(self.consumo_energia_electrica_kwh)

#! CONSTANTES: FACTORES DE EMISIÓN (CANTIDAD/CO2):
#Se crea un modelo para los factores de emisión, son constante que cambia anualmente, esto datos ingresan por el panel de administración

class Factor_emision_gas_refrigerante(models.Model):
    
    TIPO_REFRIGERANTE = models.CharField(max_length=20) #el TIPO_REFRIGERANTE puede ser: R22, entre otros
    GWP = models.FloatField() #ejemplo R22 tiene un GWP=1700.00, es un valor numérico

    class Meta:
        verbose_name = 'Tipo de Refrigerante (AR5)'
        verbose_name_plural = 'Tipos de Refrigerantes (AR5)'
    def _str_(self):
        return self.TIPO_REFRIGERANTE


class Factor_emision_consumo_energiaelectrica(models.Model):

    PAIS = models.CharField(max_length=20, default='')
    AÑO_FACTOR_EMISION = models.IntegerField(default=2020, null=True, blank=True)
    FACTOR_EMISION_ELECTRICIDAD = models.FloatField() #ejemplo factor de emisión en Colombia en el 2020 0.203

    class Meta:
        # db_table = ''
        # managed = True
        ordering = ['AÑO_FACTOR_EMISION']
        verbose_name = 'Factor de emisión por consumo de energía (kg CO2e/kWh)'
        verbose_name_plural = 'Factores de emisión por consumo de energía (kg CO2e/kWh)'

    def _str_(self):
        return self.PAIS

#! Se generar clases para los resultados de las operaciones y establecerlos en las bases de datos

class ResultadoEmisionGasRefrigerante(models.Model):

    valor = models.FloatField()

    class Meta:
        verbose_name = 'Emisión de Gas Refrigerante (KgCO2)'
        verbose_name_plural = 'Emisioes de Gases Refrigerantes (KgCO2)'
    def _str_(self):
        return self.valor

class ResultadoEmisionConsumoEnergiaelectrica(models.Model):

    valor = models.FloatField()

    class Meta:
        verbose_name = 'Emisión por Consumo de energía eléctrica (KgCO2)'
        verbose_name_plural = 'Emisiones por Consumo de energía eléctrica (KgCO2)'
    def _str_(self):
        return self.valor

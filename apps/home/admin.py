from django.contrib import admin

from . import models



# Register your models here.
admin.site.register(models.Cliente)
admin.site.register(models.Alcance1)
admin.site.register(models.Alcance2)

# Registo de los factores de emisión:
class Factor_emision_consumo_energiaelectricaAdmin(admin.ModelAdmin):
    list_display = ('PAIS', 'AÑO_FACTOR_EMISION', 'FACTOR_EMISION_ELECTRICIDAD')

admin.site.register(models.Factor_emision_consumo_energiaelectrica, Factor_emision_consumo_energiaelectricaAdmin)

class Factor_emision_gas_refrigeranteAdmin(admin.ModelAdmin):
    list_display = ('TIPO_REFRIGERANTE', 'GWP')
    
admin.site.register(models.Factor_emision_gas_refrigerante, Factor_emision_gas_refrigeranteAdmin)



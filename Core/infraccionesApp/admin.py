from django.contrib import admin
# importamos los modelos que vamos a trabajar desde el admin
from .models import Persona,Vehiculo,Oficial
# Register your models here.

class PersonaAdmin(admin.ModelAdmin):
    readonly_fields=("created","updated")#declaro los campos de solo lectura

class VehiculoAdmin(admin.ModelAdmin):
    readonly_fields=("created","updated")#declaro los campos de solo lectura

class OficialAdmin(admin.ModelAdmin):
    readonly_fields=("created","updated")#declaro los campos de solo lectura

admin.site.register(Persona,PersonaAdmin)
admin.site.register(Vehiculo,VehiculoAdmin)
admin.site.register(Oficial,OficialAdmin)
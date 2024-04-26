# Importamos de rest_framework la libreria serializers
from rest_framework import serializers # type: ignore
from infraccionesApp.models import Infraccion

class InfraccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Infraccion
        fields = ['placa_patente', 'email','timestamp', 'comentarios']
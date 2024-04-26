# Importamos de rest_framework la libreria serializers
from rest_framework import serializers # type: ignore
from infraccionesApp.models import Infraccion
# Importamos para manejar los token
from rest_framework.authtoken.models import Token # type: ignore

class InfraccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Infraccion
        fields = ['placa_patente', 'email','timestamp', 'comentarios']

# Definimos la class TokenSerializer
class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ('key', 'user', 'created')
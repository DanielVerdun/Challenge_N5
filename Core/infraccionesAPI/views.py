from django.shortcuts import render

# Create your views here.
from rest_framework import status # type: ignore
from rest_framework.views import APIView # type: ignore
from datetime import datetime  # Importa datetime para obtener la fecha y hora actuales
from infraccionesApp.models import Infraccion
from infraccionesApp.models import Persona,Vehiculo
from .serializers import InfraccionSerializer
from rest_framework.response import Response # type: ignore
from django.shortcuts import get_object_or_404
import logging


# Importamos para implementar autenticación
from rest_framework.permissions import IsAuthenticated # type: ignore
from rest_framework.authentication import TokenAuthentication # type: ignore

# Importamos para manejar los token
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token # type: ignore
from .serializers import TokenSerializer

logger = logging.getLogger(__name__)

class CargarInfraccion(APIView):
    authentication_classes = [TokenAuthentication]  # Autenticación mediante token
    permission_classes = [IsAuthenticated]  # Solo usuarios autenticados pueden acceder a esta vista

    def post(self, request):

        # Obtiene la fecha y hora actual para facilitar la carga a los oficiales
        timestamp_actual = datetime.now()

        # Crear un nuevo diccionario para los datos de la solicitud y agregar la fecha y hora actual
        datos_solicitud = request.data.copy()
        datos_solicitud["timestamp"] = timestamp_actual

        # Verificar si ya existe una persona con el correo electrónico proporcionado
        email = datos_solicitud.get('email')
        persona = get_object_or_404(Persona, email=email)

        # Asociar la nueva infracción a la persona encontrada
        datos_solicitud['persona'] = persona.id

        # Serializar los datos y guardar la infracción
        serializer = InfraccionSerializer(data=datos_solicitud)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GenerarInforme(APIView):
    def post(self, request):
        # Obtener el correo electrónico del cuerpo de la solicitud
        email = request.data.get('email')

        if not email:
            return Response({"error": "Se requiere el parámetro 'email' en el cuerpo de la solicitud"}, status=400)

        # Buscar todas las infracciones asociadas al correo electrónico proporcionado
        infracciones = Infraccion.objects.filter(email=email)

        # Serializar las infracciones encontradas
        serializer = InfraccionSerializer(infracciones, many=True)

        return Response(serializer.data)
from django.urls import path
from .views import CargarInfraccion, GenerarInforme

urlpatterns = [
    path('cargar_infraccion/', CargarInfraccion.as_view(), name='cargar_infraccion'),
    path('generar_informe/', GenerarInforme.as_view(), name='generar_informe'),
]
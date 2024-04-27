from django.db import models

# Create your models here.


class Persona(models.Model):
    nombre = models.CharField(max_length=70)
    email = models.EmailField(unique=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    class Meta:
        verbose_name = "persona"
        verbose_name_plural = "personas"

    def __str__(self):
        return self.email

class Vehiculo(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    placa_patente = models.CharField(max_length=12)
    marca = models.CharField(max_length=50)
    color = models.CharField(max_length=30)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    class Meta:
        verbose_name = "vehiculo"
        verbose_name_plural = "vehiculos"

    def __str__(self):
        return self.placa_patente

class Oficial(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    class Meta:
        verbose_name = "oficial"
        verbose_name_plural = "oficiales"

    def __str__(self):
        return str(self.id)

class Infraccion(models.Model):
    placa_patente = models.CharField(max_length=20)
    email = models.EmailField()
    timestamp = models.DateTimeField()
    comentarios = models.TextField()

    def __str__(self):
        return self.placa_patente

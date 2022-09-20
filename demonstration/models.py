import uuid as uuid
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Persona(models.Model):
    departamento = models.CharField(max_length=70)
    localidad = models.CharField(max_length=70)
    municipio = models.CharField(max_length=70)
    nombre = models.TextField(max_length=100)
    edad_activo = models.SmallIntegerField(default=0)  # Años activo
    tipo_persona = models.CharField(max_length=50)
    tipo_cargo = models.CharField(max_length=50)


class Historial(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.RESTRICT)
    porcentaje = models.FloatField(default=0.0)
    busqueda = models.CharField(max_length=100, default='')
    created = models.DateTimeField(auto_now_add=True)


class ResultadosHistorial(models.Model):
    historial = models.ForeignKey(Historial, on_delete=models.RESTRICT, related_name='resultados_historial')
    departamento = models.CharField(max_length=70)
    localidad = models.CharField(max_length=70)
    municipio = models.CharField(max_length=70)
    nombre = models.TextField(max_length=100)
    edad_activo = models.SmallIntegerField(default=0)  # Años activo
    tipo_persona = models.CharField(max_length=50)
    tipo_cargo = models.CharField(max_length=50)
    ratio = models.FloatField(default=0.0)



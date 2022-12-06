from django.db import models
from apps.users.models import User

# Create your models here.

class Especialidad(models.Model):
    """
    Especialidad de los doctores.
    """
    especialidad = models.CharField(max_length=45)
    def __str__(self):
        return self.especialidad

class Doctor(models.Model):
    """
    Doctores miembros de la Sccot que serán autores de trabajos científicos.
    """
    tipo_identificacion = models.CharField(max_length=45,null=True, blank=True)
    identificacion = models.BigIntegerField(null=True, blank=True)
    celular = models.CharField(max_length=100,null=True, blank=True)
    direccion = models.CharField(max_length=200,null=True, blank=True)
    ciudad = models.CharField(max_length=45,null=True, blank=True)
    pais = models.CharField(max_length=45,null=True, blank=True)
    especialidad = models.ForeignKey(Especialidad,null=True, blank=True, on_delete=models.CASCADE)
    usuario = models.OneToOneField(User, on_delete= models.CASCADE)
    def __str__(self):
        return f''
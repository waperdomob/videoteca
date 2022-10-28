from django.db import models

from apps.users.models import historial_user

# Create your models here.
class direccionIP(models.Model):
    direccionIP = models.CharField('Dirección IP',max_length=50)
    ciudad = models.CharField('Ciudad', max_length = 50)
    pais = models.CharField('Pais', max_length = 50)
    historial_user= models.ForeignKey(historial_user, on_delete=models.CASCADE)

#class dispositivo(models.Model):
#    dispositivo = models.CharField('Dispositivo', max_length = 50)
#    historial_user= models.ForeignKey(historial_user, on_delete=models.CASCADE)

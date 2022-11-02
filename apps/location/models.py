from django.db import models

from apps.users.models import historial_user
from apps.videos.models import historial_Video

# Create your models here.
class direccionIP(models.Model):
    direccionIP = models.CharField('Dirección IP',max_length=50)
    ciudad = models.CharField('Ciudad', max_length = 50)
    pais = models.CharField('Pais', max_length = 50)
    historial_user= models.ForeignKey(historial_user, on_delete=models.CASCADE)
    historial_Video = models.ForeignKey(historial_Video, on_delete=models.CASCADE, null=True)

#class dispositivo(models.Model):
#    dispositivo = models.CharField('Dispositivo', max_length = 50)
#    historial_user= models.ForeignKey(historial_user, on_delete=models.CASCADE)

class fechaRepro(models.Model):
    fecha = models.DateField(auto_now=True)
    historial_user = models.ForeignKey(historial_user, on_delete=models.CASCADE)
    historial_Video = models.ForeignKey(historial_Video, on_delete=models.CASCADE)
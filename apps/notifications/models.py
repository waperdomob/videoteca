from django.db import models
from apps.videos.models import  Video
from apps.users.models import Commentary

# Create your models here.

class tipoNotificacion(models.Model):
    tipo_notificacion = models.CharField('Tipo de notificación', max_length=50)

    def __str__(self):
        return f'{self.tipo_notificacion}'

class Notificaction(models.Model):
    message = models.CharField('Mensaje', max_length=45)
    created_date = models.DateTimeField('Fecha de creación', auto_now=False, auto_now_add=True)
    user_has_seen = models.BooleanField('Lectura de la notificación',default=False)
    tipo_notificacion = models.ForeignKey(tipoNotificacion, on_delete= models.CASCADE)
    video = models.ForeignKey(Video, on_delete= models.CASCADE, null=True)
    comentario = models.ForeignKey(Commentary,on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.message}'
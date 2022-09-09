from django.db import models
from simple_history.models import HistoricalRecords
# Create your models here.

class Idioma(models.Model):
    language = models.CharField('Idioma', max_length=50)
    historical = HistoricalRecords()

    class Meta:
        """Meta definition for Idioma."""

        verbose_name = 'language del video'
        verbose_name_plural = 'languages del video'

    def __str__(self):
        """Unicode representation of Idioma."""
        return self.language

class tipoVideo(models.Model):
    tipe_video = models.CharField('Idioma', max_length=50)
    historical = HistoricalRecords()

    class Meta:
        """Meta definition for tipoVideo."""

        verbose_name = 'Tipo del video'
        verbose_name_plural = 'Tipos de video'

    def __str__(self):
        """Unicode representation of tipoVideo."""
        return self.tipe_video

class Video(models.Model):
    url = models.CharField('link vimeo del video', max_length=150)
    title_espanol = models.CharField('Titulo en español', max_length=100)
    title_english = models.CharField('Titulo en ingles', max_length=100)
    title_cap_esp = models.CharField('Titulo del capitulo en español', max_length=150, blank= True, null=True)
    title_cap_esp = models.CharField('Titulo del capitulo en ingles', max_length=150, blank= True, null=True)
    description_esp = models.TextField('Descripción en español', blank= True, null=True)
    description_english = models.TextField('Descripción en ingles', blank= True, null=True)
    upload_date = models.DateTimeField('Fecha de subida', auto_now=False, auto_now_add=True)
    create_date = models.DateTimeField('Fecha de creación', blank= True, null=True)
    duration = models.DurationField(blank= True, null=True)
    featured_image = models.ImageField('Imagen destacada', upload_to=None, height_field=None, width_field=None, max_length=None)
    min_image = models.ImageField('Imagen comprimida', upload_to=None, height_field=None, width_field=None, max_length=None)
    repro_counter = models.IntegerField('Contador de reproducciones',default=0)
    score = models.DecimalField('puntuación', max_digits=5, decimal_places=2, default=5)
    tipe_of_video = models.ForeignKey(tipoVideo,on_delete=models.CASCADE)
    lenguages = models.ManyToManyField(Idioma)
    historical = HistoricalRecords()

    class Meta: 
        """Meta definition for Video."""

        verbose_name = 'Video'
        verbose_name_plural = 'Videos'

    def __str__(self):
        """Unicode representation of Video."""
        return self.title_espanol

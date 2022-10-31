
from django.db import models
from simple_history.models import HistoricalRecords
from django.forms import model_to_dict

# Create your models here.


def upload_to(instance, filename):
    return 'videos/{filename}'.format(filename=filename)

class Categoria(models.Model):
    categoria = models.CharField('Categoria', max_length=50)

    class Meta:
        """Meta definition for Categoria."""

        verbose_name = 'Categoria del video'
        verbose_name_plural = 'Categorias del video'

    def __str__(self):
        """Unicode representation of Categoria."""
        return self.categoria
class Idioma(models.Model):
    language = models.CharField('Idioma', max_length=50)

    class Meta:
        """Meta definition for Idioma."""

        verbose_name = 'language del video'
        verbose_name_plural = 'languages del video'

    def __str__(self):
        """Unicode representation of Idioma."""
        return self.language

class tipoVideo(models.Model):
    tipe_video = models.CharField('Tipo de video', max_length=50)

    class Meta:
        """Meta definition for tipoVideo."""

        verbose_name = 'Tipo del video'
        verbose_name_plural = 'Tipos de video'

    def __str__(self):
        """Unicode representation of tipoVideo."""
        return self.tipe_video

class Video(models.Model):
    code_esp = models.CharField('Código del video en español de vimeo', max_length=150, null=True,blank= True,unique=True)
    code_engl = models.CharField('Código del video en ingles de vimeo', max_length=150, null=True,blank= True,unique=True)
    url_vimeo_esp = models.CharField('url del video en español de vimeo', max_length=150, null=True,blank= True)
    url_vimeo_eng = models.CharField('url del video en ingles de vimeo', max_length=150, null=True,blank= True)
    title_espanol = models.CharField('Titulo en español', max_length=100)
    title_english = models.CharField('Titulo en ingles', max_length=100)
    title_cap_esp = models.CharField('Titulo del capitulo en español', max_length=150, blank= True, null=True)
    title_cap_english = models.CharField('Titulo del capitulo en ingles', max_length=150, blank= True, null=True)
    description_esp = models.TextField('Descripción en español', blank= True, null=True)
    description_english = models.TextField('Descripción en ingles', blank= True, null=True)
    upload_date = models.DateTimeField('Fecha de subida', auto_now=False, auto_now_add=True)
    create_date = models.DateTimeField('Fecha de creación', blank= True, null=True)
    duration = models.DurationField('Duración',blank= True, null=True)
    featured_image = models.ImageField('Imagen destacada', upload_to=upload_to, null=True, blank=True,height_field=None, width_field=None, max_length=None)
    min_image = models.ImageField('Imagen comprimida', upload_to=upload_to, null=True, blank=True,height_field=None, width_field=None, max_length=None)
    repro_counter = models.IntegerField('Contador de reproducciones',default=0)
    score = models.DecimalField('puntuación', max_digits=3, decimal_places=2, null=True)
    tipe_of_video = models.ForeignKey(tipoVideo,on_delete=models.CASCADE, verbose_name='Tipo de video')
    categorias = models.ManyToManyField(Categoria, related_name="Categorias", verbose_name="Categorias")
    languages = models.ManyToManyField(Idioma, related_name="Idiomas", verbose_name='Idiomas')
    state = models.BooleanField('Estado',default = True)

    class Meta: 
        """Meta definition for Video."""

        verbose_name = 'Video'
        verbose_name_plural = 'Videos'

    def get_lenguages_video(self):
        return Idioma.objects.filter(Idiomas = self)

    def get_categories_video(self):
        return Categoria.objects.filter(Categorias = self)

    def __str__(self):
        """Unicode representation of Video."""
        return self.title_espanol

    #def toJSON(self):
    #    item = model_to_dict(self)
    #    item['score'] = format(self.score, '.2f')
    #    return item
class historial_Video(models.Model):
    reproducciones = models.IntegerField(default=0)
    video = models.ForeignKey(Video, on_delete= models.CASCADE)

    def __str__(self):
        return f'{self.id}'
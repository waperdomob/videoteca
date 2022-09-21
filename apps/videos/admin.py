from django.contrib import admin
from apps.videos.models import *
# Register your models here.

class idiomaAdmin(admin.ModelAdmin):
    list_display = ('id','language')

class tipoVideoAdmin(admin.ModelAdmin):
    list_display = ('id','tipe_video')

admin.site.register(Idioma,idiomaAdmin)
admin.site.register(tipoVideo,tipoVideoAdmin)
admin.site.register(Video)

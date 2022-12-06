from django.contrib import admin
from apps.videos.models import *
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class categoriaAdmin(admin.ModelAdmin):
    list_display = ('id','categoria')
class idiomaAdmin(admin.ModelAdmin):
    list_display = ('id','language')

class tipoVideoAdmin(admin.ModelAdmin):
    list_display = ('id','tipe_video')

admin.site.register(Categoria,categoriaAdmin)
admin.site.register(Idioma,idiomaAdmin)
admin.site.register(tipoVideo,tipoVideoAdmin)
admin.site.register(Video)

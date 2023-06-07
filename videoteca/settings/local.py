from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'sql_mode': 'traditional',
        },
        'NAME': 'videoteca2',
        'USER':'root',
        'PASSWORD':'',
        'HOST':'localhost',
        'PORT':'3306'
    },
    'trabajos': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'sql_mode': 'traditional',
        },
        'NAME': 'trabajos',
        'USER':'root',
        'PASSWORD':'',
        'HOST':'localhost',
        'PORT':'3306'
    }
}



#DATABASE_ROUTERS=['videoteca_db','trabajos_db']

#DATABASE_APPS_MAPPING = {
     # example:
     # 'app_name':'database_name',
     #'venncheck': 'skucheck',
     #'barcode': 'barcode',
     #'catecheck': 'catecheck',
     #'clust': 'vip_cluster',
     #'the_entrance': 'venn',
     #'admin': 'videoteca_db',
     #'auth': 'videoteca_db',
     #'contenttypes': 'videoteca_db',
     #'sessions': 'videoteca_db',
#}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
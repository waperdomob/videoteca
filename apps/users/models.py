from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser , PermissionsMixin
from django.forms import model_to_dict


from videoteca.settings.base import MEDIA_URL, STATIC_URL


class userRole(models.Model):
    role = models.CharField(max_length=45)

    def __str__(self):
        return self.role

class UserManager(BaseUserManager):
    def _create_user(self, user_login,name, email, password, is_staff, is_superuser, **extra_fields):
        user = self.model(
            user_login = user_login,
            name = name,
            email = email,
            is_staff = is_staff,
            is_superuser = is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, user_login, name, email,  password=None, **extra_fields):
        return self._create_user(user_login, name, email,  password, False, False, **extra_fields)

    def create_superuser(self, user_login,name, email, password=None, **extra_fields):
        return self._create_user(user_login,name, email,  password, True, True, **extra_fields)

class User(AbstractBaseUser , PermissionsMixin):

    user_login = models.CharField(max_length = 255, unique = True)
    name = models.CharField('Nombre completo', max_length = 255, blank = True, null = True)
    email = models.EmailField('Correo Electrónico',max_length = 255, unique = True)
    user_url = models.CharField('url del usuario', max_length = 255, blank = True, null = True)
    is_superuser = models.BooleanField(default = False)
    is_staff = models.BooleanField(default = False)
    is_active = models.BooleanField(default = True) 
    date_joined= models.DateTimeField('fecha de registro', auto_now_add= True)
    date_update = models.DateTimeField('fecha de actualizacion', auto_now= True)
    login_check = models.BooleanField('Validacion si esta online', blank = True, null = True)
    image = models.ImageField('Imagen de perfil', upload_to='perfil/', max_length=255, null=True, blank = True)
    role = models.ForeignKey(userRole, blank=True, null=True, on_delete=models.CASCADE)
    objects = UserManager()
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    USERNAME_FIELD = 'user_login'
    REQUIRED_FIELDS = ['email','name']

    def get_image(self):
        if self.image:
            return '{}{}'.format(MEDIA_URL, self.image)
        return '{}{}'.format(STATIC_URL, 'img/empty.png')

    def toJSON(self):
        item = model_to_dict(self, exclude=['password', 'user_permissions', 'last_login'])
        if self.last_login:
            item['last_login'] = self.last_login.strftime('%Y-%m-%d')
        item['date_joined'] = self.date_joined.strftime('%Y-%m-%d')
        item['date_update'] = self.date_update.strftime('%Y-%m-%d')
        item['image'] = self.get_image()
        item['groups'] = [{'id': g.id, 'name': g.name} for g in self.groups.all()]
        return item

    def natural_key(self):
        return (self.user_login)

    def __str__(self):
        return f'{self.name}'

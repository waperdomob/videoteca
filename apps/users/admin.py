from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from apps.users.models import User,userRole
class userRoleAdmin(admin.ModelAdmin):
    list_display = ('id','role')

admin.site.register(User)
admin.site.register(userRole,userRoleAdmin)

from django.contrib import admin
from .models import *
# Register your models here.

#admin.site.register(Rol)

@admin.register(Rol)
class RolAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')

from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(Logo)
class LogoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
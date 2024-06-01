from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_surname', 'description', 'position',)
    list_filter = ('id', 'name_surname', 'description', 'photo', 'position',)

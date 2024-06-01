from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'date',)
    list_filter = ('id', 'title', 'description', 'photo', 'date',)
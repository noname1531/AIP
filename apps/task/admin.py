from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'completed', 'date',)
    list_filter = ('id', 'title', 'description', 'completed', 'date',)
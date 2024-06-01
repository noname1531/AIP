from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='Название задачи'
    )
    description = models.TextField(
        verbose_name="Описание задачи",
    )
    completed = models.BooleanField(
        default=False
    )
    date = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Время создания зодачи"
    )
    
    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"
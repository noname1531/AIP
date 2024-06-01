from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='Нзвание'
    )
    description = models.TextField(
        verbose_name="Описание",
    )
    photo = models.ImageField(
        upload_to="photo/",
        verbose_name="Фото"
    )
    date = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата публикации"
    )
    
    class Meta:
        verbose_name = "Новосная строница"
        verbose_name_plural = "Новосная строница"
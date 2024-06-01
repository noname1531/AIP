from django.db import models

# Create your models here.
class Logo(models.Model):
    logo = models.ImageField(
        upload_to="logo/",
        verbose_name="Логотип",
    )
    title = models.CharField(
        max_length=100,
        verbose_name="Название",
    )
    description = models.TextField(
        verbose_name="Описание",
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Главная строница"
        verbose_name_plural = "Главная строница"
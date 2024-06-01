from django.db import models

# Create your models here.
class Team(models.Model):
    name_surname = models.CharField(
        max_length=100,
        verbose_name="ФИО",
    )
    photo = models.ImageField(
        upload_to="photo/",
        verbose_name="Фото",
    )
    description = models.TextField(
        verbose_name="Описание",
    )
    position = models.CharField(
        max_length=100,
        verbose_name="Должность",
    )

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"
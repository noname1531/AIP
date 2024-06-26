# Generated by Django 5.0.6 on 2024-06-01 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_surname', models.CharField(max_length=100, verbose_name='ФИО')),
                ('photo', models.ImageField(upload_to='photo/', verbose_name='Фото')),
                ('description', models.TextField(verbose_name='Описание')),
                ('position', models.CharField(max_length=100, verbose_name='Должность')),
            ],
            options={
                'verbose_name': 'Сотрудник',
                'verbose_name_plural': 'Сотрудники',
            },
        ),
    ]

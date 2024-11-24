from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.CharField(max_length=150, verbose_name='Описание')
    image = models.ImageField(upload_to='catalog/image', blank=True, null=True, verbose_name='Изображение')
    category = models.CharField(max_length=150, verbose_name='Категория')
    purchase_price = models.FloatField(max_length=100, verbose_name='цена за покупку')
    created_at = models.DateField( blank=True, null=True, verbose_name='Дата создания')
    updated_at = models.DateField( blank=True, null=True, verbose_name='Дата последнего изменения')

    def __str__(self):
        return f'{self.name} {self.description}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ['name']


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.CharField(max_length=150, verbose_name='Описание')

    def __str__(self):
        return f'{self.name} {self.description}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'




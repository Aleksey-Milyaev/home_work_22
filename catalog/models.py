from django.db import models

from users.models import User


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.CharField(max_length=150, verbose_name='Описание')

    def __str__(self):
        return f'{self.name} {self.description}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.CharField(max_length=150, verbose_name='Описание')
    image = models.ImageField(upload_to='blog/image', blank=True, null=True, verbose_name='Изображение')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    purchase_price = models.FloatField(max_length=100, verbose_name='цена за покупку')
    created_at = models.DateField(blank=True, null=True, verbose_name='Дата создания')
    updated_at = models.DateField(blank=True, null=True, verbose_name='Дата последнего изменения')
    publication = models.BooleanField(default=False, verbose_name='Статус публикации')
    owner = models.ForeignKey(User, verbose_name='имя владельца', blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.name} {self.description}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ['name']
        permissions = [
            ('can_un_publish_product', 'Can un publish product'),
        ]

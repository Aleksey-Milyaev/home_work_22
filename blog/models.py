from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    context = models.CharField(max_length=150, verbose_name='Содержимое')
    image = models.ImageField(upload_to='blog/image', blank=True, null=True, verbose_name='Изображение')
    created_at = models.DateField(blank=True, null=True, verbose_name='Дата создания')
    publication = models.BooleanField(max_length=100, verbose_name='публикация', default=True)
    number_views = models.PositiveIntegerField(verbose_name="Количество просмотров",
                                               help_text="Укажите количество просмотров", default=0,)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'

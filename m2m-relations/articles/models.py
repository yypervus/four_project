from django.db import models


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)
    scopes = models.ManyToManyField('Scope', related_name='articles', through="ArticleInScope")

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


class Scope(models.Model):
    topic = models.CharField(verbose_name="Тег", max_length=254)

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'
        ordering = ['-articleinscope__is_main', 'topic']

    def __str__(self):
        return f'{self.topic}'


class ArticleInScope(models.Model):
    article = models.ForeignKey(Article, verbose_name="Статья", on_delete=models.CASCADE)
    scope = models.ForeignKey(Scope, verbose_name="Раздел", on_delete=models.CASCADE)
    is_main = models.BooleanField(verbose_name="Основной", default=False)

    class Meta:
        verbose_name = 'Тематика статьи'
        verbose_name_plural = 'Тематики статьи'


    def __str__(self):
        return f'{self.article}'

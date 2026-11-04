from django.db import models


class Article(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name="Заголовок",
    )

    content = models.TextField(
        verbose_name="Текст новости",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания",
    )

    is_published = models.BooleanField(
        default=False,
        verbose_name="Опубликована",
    )

    author = models.CharField(
        max_length=100,
        default="Редакция",
        verbose_name="Автор",
    )

    category = models.CharField(
        max_length=100,
        default="Общее",
        verbose_name="Категория",
    )

    def __str__(self):
        return self.title


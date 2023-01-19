from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Group(models.Model):
    title = models.CharField('Название', max_length=200)
    slug = models.SlugField('Идентификатор', unique=True)
    description = models.TextField('Описание', max_length=100)

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField('Текст поста')
    pub_date = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True
    )
    author = models.ForeignKey(
        User,
        verbose_name='Автор',
        on_delete=models.CASCADE,
        related_name='posts'
    )
    group = models.ForeignKey(
        Group,
        verbose_name='Группа',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='posts'
    )

    class Meta:
        ordering = ('-pub_date',)

    def __str__(self):
        """Возвращаем автора, дату публикации, пост 15 символов."""
        return (f'Автор: , {self.author}',
                f'Дата публикации: , {self.pub_date}',
                f'Пост: , {self.text[:15]}')

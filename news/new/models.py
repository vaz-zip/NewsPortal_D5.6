from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    author_user = models.OneToOneField(User, on_delete=models.CASCADE)
    author_rating = models.SmallIntegerField(default=0)

    def __str__(self):
        return f'{self.author_user}'

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    def get_absolute_url(self):
        return f'/user_edit/{self.id}/'


class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return f'{self.name}'


article = 'СТА'
news = 'НОВ'

POSITIONS = [
    (article, 'Статья'),
    (news, 'Новость')
]


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.CharField(max_length=3, choices=POSITIONS, default=news)
    time_public = models.DateTimeField(auto_now_add=True, verbose_name='Опубликовано')
    post_category = models.ManyToManyField(Category, through='PostCategory')
    title = models.CharField(max_length=128, verbose_name='Заголовок')
    text = models.TextField(null=True, blank=True, verbose_name='Текст')
    rating = models.IntegerField(default=0, verbose_name='Рейтинг')

    def __str__(self):
        return f'{self.title} {self.time_public}'

    def get_absolute_url(self):
        return f'/news/{self.id}'

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def date(self):
        return f'{self.time_public.strftime("%d. %m. %Y")}'


class PostCategory(models.Model):
    post_category_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    post_category_category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    comment_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_us = models.TextField()
    time_comment = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

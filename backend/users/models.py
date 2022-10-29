from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):

    email = models.EmailField(
        db_index=True,
        unique=True,
        max_length=254,
        verbose_name='Электронная почта пользователя',
        help_text='Введите электронную почту пользователя')
    username = models.CharField(
        db_index=True,
        max_length=150,
        unique=True,
        verbose_name='Уникальное имя пользователя',
        help_text='Введите уникальное имя пользователя')
    first_name = models.CharField(
        max_length=150,
        verbose_name='Имя пользователя',
        help_text='Введите имя пользователя')
    last_name = models.CharField(
        max_length=150,
        verbose_name='Фамилия пользователя',
        help_text='Введите фамилию пользователя')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'password']

    def __str__(self):
        return self.username


class Follow(models.Model):
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        verbose_name='Подписчик',
        related_name='follower'
    )
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        verbose_name='Автор на которого подписан',
        related_name='following'
    )

    class Meta:
        ordering = ['user', 'author']
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'author'],
                name='unique_follow'
            )
        ]

    def __str__(self):
        return f'{self.user} -> {self.author}'

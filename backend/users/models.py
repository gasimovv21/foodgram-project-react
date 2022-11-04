from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models


class CustomUser(AbstractUser):

    email = models.EmailField(
        db_index=True,
        unique=True,
        max_length=settings.MAX_LENGTH_EMAIL,
        verbose_name='Электронная почта пользователя',
        help_text='Введите электронную почту пользователя')
    username = models.CharField(
        db_index=True,
        max_length=settings.MAX_LENGTH_USERNAME,
        unique=True,
        validators=[RegexValidator(
            regex=r'^[\w.@+-]+\Z',
            message='Введите корректный Никнэйм',
            code='invalid_username')],
        verbose_name='Никнэйм пользователя',)
    first_name = models.CharField(
        max_length=settings.MAX_LENGTH_FIRST_NAME,
        verbose_name='Имя пользователя',
        help_text='Введите имя пользователя')
    last_name = models.CharField(
        max_length=settings.MAX_LENGTH_LAST_NAME,
        verbose_name='Фамилия пользователя',
        help_text='Введите фамилию пользователя')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username', 'first_name', 'last_name', 'password')

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
            ),
            models.CheckConstraint(
                name="%(app_label)s_%(class)s_prevent_self_follow",
                check=~models.Q(user=models.F("author")),
            )
        ]

    def __str__(self):
        return f'{self.user} -> {self.author}'

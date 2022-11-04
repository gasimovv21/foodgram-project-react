from django.core.validators import MinValueValidator
from django.conf import settings
from django.db import models

from users.models import CustomUser


class Tag(models.Model):
    name = models.CharField(
        max_length=settings.MAX_LENGTH_TAG_NAME,
        verbose_name='Название тэга'
    )
    color = models.CharField(
        max_length=settings.MAX_LENGTH_TAG_COLOR,
        verbose_name='Цвет тэга'
    )
    slug = models.SlugField(
        max_length=settings.MAX_LENGTH_TAG_SLUG,
        verbose_name='Уникальный номер тэга'
    )

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(
        max_length=settings.MAX_LENGTH_INGREDIENT_NAME,
        verbose_name='Название ингредиента'
    )
    measurement_unit = models.CharField(
        max_length=settings.MAX_LENGTH_INGREDIENT_MEASURMENT_UNIT,
        verbose_name='Единица измерения ингредиента'
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'

    def __str__(self):
        return self.name


class Recipe(models.Model):
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        verbose_name='Автор рецепта',
        related_name='recipes'
    )
    name = models.CharField(
        max_length=settings.MAX_LENGTH_RECIPE_NAME,
        verbose_name='Название рецепта'
    )
    image = models.ImageField(
        verbose_name='Картинка рецепта',
        upload_to='recipes/'
    )
    text = models.TextField(
        verbose_name='Описание рецепта'
    )
    cooking_time = models.PositiveSmallIntegerField(
        verbose_name='Время приготовления рецепта',
        validators=[MinValueValidator(
            1,
            message='Минимальное время приготовления'
                    'должно быть больше или равно 1 мин!')]
    )
    ingredients = models.ManyToManyField(
        Ingredient,
        through='IngredientInRecipe',
        verbose_name='Ингредиенты рецепта'
    )
    tags = models.ManyToManyField(
        Tag,
        blank=True,
        verbose_name='Тэги рецепта'
    )

    class Meta:
        ordering = ['name']
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def show_ingredients(self):

        return " %s" % (', '.join([ingredient.name for ingredient in self.ingredients.all()]))
    show_ingredients.short_description = 'Ингредиенты'

    def __str__(self):
        return self.name


class IngredientInRecipe(models.Model):
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        verbose_name='Рецепт',
    )
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        verbose_name='Ингредиента',
    )
    amount = models.PositiveIntegerField(
        null=True,
        verbose_name='Количество',
        validators=[MinValueValidator(
            1,
            message='Минимальное количество ингредиентов'
                    'должно быть больше нуля!')]
    )

    class Meta:
        ordering = ['recipe']
        verbose_name = 'Ингредиент рецепта'
        verbose_name_plural = 'Ингредиенты рецепта'
        constraints = [
            models.UniqueConstraint(
                fields=['recipe', 'ingredient', 'amount'],
                name='unique_ingredient_in_recipe')]


class ShoppingCart(models.Model):
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        related_name='shoping_cart_owner'
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        verbose_name='Товар',
        related_name='shopping_cart_recipe',
    )

    class Meta:
        ordering = ['recipe']
        verbose_name = 'Список товара'
        verbose_name_plural = 'Списки товаров'
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'recipe'],
                name='unique_shopping_cart')]


class Favorite(models.Model):
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        related_name='favorite_subscriber'
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        verbose_name='Рецепт',
        related_name='favorites'
    )

    class Meta:
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранное'

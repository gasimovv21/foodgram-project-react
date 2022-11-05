from django.contrib import admin

from .models import (Favorite, Ingredient, IngredientInRecipe, Recipe,
                     ShoppingCart, Tag)


class IngredientsInline(admin.StackedInline):

    model = IngredientInRecipe
    extra = 5


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    empty_value_display = '-пусто-'


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'measurement_unit')
    list_filter = ('name',)
    search_fields = ('name',)
    empty_value_display = '-пусто-'


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    inlines = [IngredientsInline]
    list_display = ('id', 'name', 'author', 'count_favorite',
                    'show_ingredients')
    list_filter = ('author', 'name', 'tags')
    search_fields = ('name',)
    empty_value_display = '-пусто-'

    @staticmethod
    def count_favorite(obj):

        return obj.favorites.count()
    count_favorite.short_description = 'Количество добавлении в избранное'

    @staticmethod
    def show_ingredients(obj):

        return " %s" % (', '.join([obj.ingredient.name for obj.ingredient in obj.ingredients.all()]))
    show_ingredients.short_description = 'Ингредиенты'


@admin.register(IngredientInRecipe)
class IngredientInRecipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'ingredient', 'recipe', 'amount')
    empty_value_display = '-пусто-'


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'recipe')
    empty_value_display = '-пусто-'


@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'recipe')
    empty_value_display = '-пусто-'

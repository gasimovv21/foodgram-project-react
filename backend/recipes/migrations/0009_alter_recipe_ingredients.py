# Generated by Django 3.2.16 on 2022-11-05 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0008_alter_recipe_ingredients'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=models.ManyToManyField(through='recipes.IngredientInRecipe', to='recipes.Ingredient', verbose_name='Ингредиенты рецепта'),
        ),
    ]

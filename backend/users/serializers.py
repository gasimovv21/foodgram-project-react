from djoser.serializers import UserCreateSerializer, UserSerializer
from recipes.models import Recipe
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import CustomUser, Follow


class CustomUserCreateSerializer(UserCreateSerializer):

    class Meta(UserCreateSerializer.Meta):
        model = CustomUser
        fields = (
            'email',
            'id',
            'username',
            'first_name',
            'last_name',
            'password'
        )


class CustomUserSerializer(UserSerializer):
    is_subscribed = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = CustomUser
        fields = ('email', 'id', 'username', 'first_name',
                  'last_name', 'is_subscribed')

    def get_is_subscribed(self, obj):
        request = self.context.get('request')
        if not request.user.is_anonymous:
            return Follow.objects.filter(
                user=request.user, author=obj).exists()
        return False


class FollowSerializer(serializers.ModelSerializer):

    class Meta:
        model = Follow
        fields = '__all__'
        ordering = ['-id']
        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=('user', 'author'),
                message='Нельзя повторно подписаться на автора.'
            )
        ]

    def to_representation(self, instance):
        request = self.context.get('request')
        context = {'request': request}
        return ShowFollowersSerializer(instance.author, context=context).data


class FollowRecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ('id', 'name', 'image', 'cooking_time')
        ordering = ['-id']


class ShowFollowersSerializer(serializers.ModelSerializer):

    recipes = serializers.SerializerMethodField(read_only=True)
    recipes_count = serializers.SerializerMethodField(read_only=True)
    is_subscribed = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = CustomUser
        fields = ('email', 'id', 'username', 'first_name',
                  'last_name', 'is_subscribed', 'recipes', 'recipes_count')
        ordering = ['-id']

    def get_is_subscribed(self, obj):
        request = self.context.get('request')
        if not request.user.is_anonymous:
            return Follow.objects.filter(
                user=request.user, author=obj).exists()
        return False

    def get_recipes(self, obj):
        request = self.context.get('request')
        if not request.user.is_anonymous:
            context = {'request': request}
            recipes_limit = request.query_params.get('recipes_limit')
        else:
            return False
        if recipes_limit is not None:
            recipes = obj.recipes.all()[:int(recipes_limit)]
        else:
            recipes = obj.recipes.all()
        return FollowRecipeSerializer(recipes, many=True, context=context).data

    def get_recipes_count(self, obj):
        return obj.recipes.count()

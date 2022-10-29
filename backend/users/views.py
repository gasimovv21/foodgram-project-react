from rest_framework import status
from rest_framework.generics import ListAPIView, get_object_or_404
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import CustomUser, Follow
from .serializers import FollowSerializer, ShowFollowersSerializer


class FollowView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, id):
        user = request.user
        data = {'user': user.id, 'author': id}
        serializer = FollowSerializer(data=data, context={'request': request})
        if user.id == id:
            return Response(
                'Нельзя подписываться на самого себя.',
                status=status.HTTP_400_BAD_REQUEST)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, id):
        user = request.user
        following = get_object_or_404(CustomUser, id=id)
        follow = get_object_or_404(Follow, user=user, author=following)
        if user.id == follow.id:
            return Response(
                'Вы не можете отписаться не имея подписку на автора.',
                status=status.HTTP_400_BAD_REQUEST)
        follow.delete()
        return Response(
            'Вы успешно отписались от автора.',
            status=status.HTTP_204_NO_CONTENT)


class FollowListView(ListAPIView):
    pagination_class = PageNumberPagination
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user = request.user
        queryset = CustomUser.objects.filter(following__user=user)
        page = self.paginate_queryset(queryset)
        serializer = ShowFollowersSerializer(
            page, many=True, context={'request': request})
        return self.get_paginated_response(serializer.data)

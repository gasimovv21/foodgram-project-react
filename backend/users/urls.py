from django.urls import include, path

from .views import FollowListView, FollowView

urlpatterns = [
    path('users/<int:id>/subscribe/', FollowView.as_view(),
         name='subscribe'),
    path('users/subscriptions/', FollowListView.as_view(),
         name='subscription'),
    path('', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]

# # Routers provide an easy way of automatically determining the URL conf.
# from django.urls import include, path
# from rest_framework import routers
#
# from api2.views import UserViewSet, PostViewSet, CommentViewSet
#
# router = routers.DefaultRouter()
# router.register(r'user', UserViewSet)
# router.register(r'post', PostViewSet)
# router.register(r'comment', CommentViewSet)
#
# # Wire up our API using automatic URL routing.
# # Additionally, we include login URLs for the browsable API.
# urlpatterns = [
#     path('', include(router.urls)),
# ]
from django.urls import path

from api2 import views

urlpatterns = [
    path('post/', views.PostListAPIView.as_view(), name='post-list'),
    path('post/<int:pk>/', views.PostRetrieveAPIView.as_view(), name='post-detail'),
    path('comment/', views.CommentCreateAPIView.as_view(), name='comment-list'),
    path('post/<int:pk>/like/', views.PostLikeAPIView.as_view(), name='post-like'),
]
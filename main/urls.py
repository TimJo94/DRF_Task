from django.urls import path, include
from rest_framework.routers import DefaultRouter

from main.views import PostListView, PostCreateView, PostUpdateView, PostDeleteView, CommentViewSet, CommentListView

router = DefaultRouter()
router.register('comments', CommentViewSet)


urlpatterns = [
    path('post-create/', PostCreateView.as_view()),
    path('posts-list/', PostListView.as_view()),
    path('post-update/<int:pk>/', PostUpdateView.as_view()),
    path('post-delete/<int:pk>/', PostDeleteView.as_view()),
    path('', include(router.urls)),
    path('comments-list/', CommentListView.as_view())

]
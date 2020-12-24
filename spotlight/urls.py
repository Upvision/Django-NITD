from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'spotlight'

router = DefaultRouter()
router.register('categories', views.CategoryViewSet, basename='categories')
router.register('posts', views.PostViewSet, basename='posts')
router.register('reacts', views.PostReactViewSet, basename='reacts')
router.register('comments', views.PostCommentViewSet, basename='comments')
router.register('replies', views.PostCommentReplyViewSet, basename='replies')
urlpatterns = router.urls


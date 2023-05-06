from django.urls import path, include
from rest_framework import routers
from .views import (
    CommentNameViewSet,
    CommentViewViewSet,
    CommentStarViewSet,
    CommentImageViewSet,
    CommentTextViewSet,
    BlogPostViewSet,
    FormQuestionViewSet,
)

router = routers.DefaultRouter()
router.register(r'name', CommentNameViewSet)
router.register(r'view', CommentViewViewSet)
router.register(r'star', CommentStarViewSet)
router.register(r'image', CommentImageViewSet)
router.register(r'text', CommentTextViewSet)
router.register(r'blog_post', BlogPostViewSet)
router.register(r'form_question', FormQuestionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
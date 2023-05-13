from django.urls import path, include
from rest_framework import routers
from .views import (
    CommentNameViewSet,
    CommentViewViewSet,
    CommentStarViewSet,
    CommentImageViewSet,
    CommentTextViewSet,
    ChooseTourViewSet
)

router = routers.DefaultRouter()
router.register(r'name', CommentNameViewSet)
router.register(r'view', CommentViewViewSet)
router.register(r'star', CommentStarViewSet)
router.register(r'ChooseTour', ChooseTourViewSet)
router.register(r'image', CommentImageViewSet)
router.register(r'text', CommentTextViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
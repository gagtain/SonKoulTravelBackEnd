from django.urls import path, include
from rest_framework import routers
from .views import CommentViewViewSet

router = routers.DefaultRouter()
router.register(r'comment', CommentViewViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

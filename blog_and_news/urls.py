from django.urls import path, include
from rest_framework import routers

from .serializers import BodySerializer
from .views import (
    BlogViewSet,
    BodyViewSet
)

router = routers.DefaultRouter()
router.register(r'blog', BlogViewSet)
router.register(r'body', BodyViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
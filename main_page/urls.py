from django.urls import path, include
from rest_framework import routers

from .views import FormQuestionViewSet

router = routers.DefaultRouter()
router.register(r'questions', FormQuestionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
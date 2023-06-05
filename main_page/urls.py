from django.urls import path, include
from rest_framework import routers

from main_page.views import FormQuestionViewSet

router = routers.SimpleRouter()
router.register(r'questions', FormQuestionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
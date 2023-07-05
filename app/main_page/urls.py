from django.urls import path, include
from rest_framework import routers

from main_page.views import FormQuestionViewSet, OurTeamViewSet

router = routers.DefaultRouter()
router.register(r'questions', FormQuestionViewSet)
router.register(r'ourteam', OurTeamViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
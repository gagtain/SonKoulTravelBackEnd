from django.urls import path, include
from rest_framework import routers
from .views import (
    TourAddViewSet,
    TourProgramViewSet,
    PriceViewSet,
    TipsViewSet,
    PhotoViewSet
)

router = routers.DefaultRouter()
router.register(r'TourAdd', TourAddViewSet)
router.register(r'TourProgram', TourProgramViewSet)
router.register(r'Price', PriceViewSet)
router.register(r'Tips', TipsViewSet)
router.register(r'Photo', PhotoViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
from django.urls import path, include
from rest_framework import routers
from .views import (
    TourAddViewSet,
    TourProgramViewSet,
    PriceViewSet,
    TipsViewSet,
    PhotoViewSet,
    TourDateViewSet,
    BookingGroupTourViewSet,
    BookingPrivateTourViewSet
)

router = routers.DefaultRouter()
router.register(r'TourAdd', TourAddViewSet)
router.register(r'TourProgram', TourProgramViewSet)
router.register(r'Price', PriceViewSet)
router.register(r'Tips', TipsViewSet)
router.register(r'Photo', PhotoViewSet)
router.register(r'TourDate', TourDateViewSet)
router.register(r'BookingGroupTour', BookingGroupTourViewSet)
router.register(r'BookingPrivateTour', BookingPrivateTourViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
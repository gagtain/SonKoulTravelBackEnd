import requests
from django.db.migrations import serializer
from rest_framework import viewsets, status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
import telegram
from rest_framework import status
from rest_framework.views import APIView

from .serializers import (
    BlogSerializer,
    BodySerializer
)

from .models import (
    BlogNews,
    Body
)

from .filters import (
    BlogFilter
)


class BlogViewSet(viewsets.ModelViewSet):
    queryset = BlogNews.objects.all()
    serializer_class = BlogSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = BlogFilter


class BodyViewSet(viewsets.ModelViewSet):
    queryset = Body.objects.all()
    serializer_class = BodySerializer

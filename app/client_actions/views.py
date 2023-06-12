import os
import requests

from rest_framework import viewsets, status, permissions
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser
from rest_framework import mixins, viewsets, status
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from datetime import timedelta
from django.utils import timezone
from rest_framework.pagination import PageNumberPagination

from .compress_image import compress_image
from .filters import CommentFilter
from .models import (
    CommentView,
    Photo

)

from .serializers import (
    CommentViewSerializer,
    PhotoSerializer

)


class CommentViewViewSet(viewsets.ModelViewSet):
    queryset = CommentView.objects.all()
    serializer_class = CommentViewSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = CommentFilter
    ordering_fields = ['date', 'stars']
    allowed_actions = ['create', 'list', 'retrieve']

    def get_permissions(self):
        if self.action == 'destroy' or self.action == 'update':
            permission_classes = [permissions.IsAdminUser]
        else:
            permission_classes = [permissions.AllowAny]
        permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]

    def list(self, request, *args, **kwargs):
        if not request.user.is_staff:  # Проверяем, является ли пользователь администратором
            queryset = self.filter_queryset(self.get_queryset().filter(is_approved=True))
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        else:
            return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        super().create(request, *args, **kwargs)
        mutable_data = request.data
        mutable_data["is_approved"] = False
        mutable_data["at_moderation"] = timezone.now()
        serializer = CommentViewSerializer(data=mutable_data)
        if serializer.is_valid():
            # Отправка ответа на клиент
            responce_201 = {
                "message": "Спасибо за ваш отзыв! Ваш комментарий был успешно отправлен на модерацию и будет опубликован, как только пройдет проверку."
            }
            headers = self.get_success_headers(serializer.data)
            return Response(responce_201, status=status.HTTP_201_CREATED, headers=headers)
        responce_400 = {
            "message": "Упс! Что-то пошло не так. Разработчики уже работают над исправлением, и вы сможете добавить комментарии снова.",
            "data": serializer.errors
        }
        return Response(responce_400, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        mutable_data = request.data.copy()
        mutable_data["is_approved"] = request.data.get("is_approved", instance.is_approved)

        if not instance.is_approved and instance.moderated_at is not None:
            two_days_ago = timezone.now() - timedelta(days=2)
            if instance.moderated_at <= two_days_ago:
                # Удаление комментария, если прошло 2 дня без действий со стороны администраторов
                instance.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)

        serializer = CommentViewSerializer(instance, data=mutable_data)
        if serializer.is_valid() and permissions.IsAdminUser():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK) and super().update(request, *args, **kwargs)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if self.request.user.is_staff:  # Check if the user is an admin
            instance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        response_403 = {
            "message": "Insufficient permissions! Only admins can delete comments."
        }
        return Response(response_403, status=status.HTTP_403_FORBIDDEN)


class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

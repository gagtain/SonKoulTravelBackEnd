import os
import requests


from rest_framework import viewsets, status, permissions
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser
from rest_framework import mixins, viewsets, status
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from datetime import timedelta
from django.utils import timezone
from rest_framework.pagination import PageNumberPagination

from .models import (
    CommentView,
)

from .serializers import (
    CommentViewSerializer,
)


class TelegramMixin:
    def send_telegram_message(self, message):
        bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
        chat_id = os.getenv('TELEGRAM_CHAT_ID')
        url = f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={message}'
        try:
            response = requests.post(url)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            raise APIException('Error while sending Telegram message') from e


class CommentNameViewSet(viewsets.ModelViewSet):
    queryset = CommentName.objects.all()
    serializer_class = CommentNameSerializer


class MyPagination(PageNumberPagination):
    page_size = 6  # Количество элементов на одной странице
    page_query_param = 'page'  # Название параметра запроса, содержащего номер страницы
    page_size_query_param = 'page_size'  # Название параметра запроса, содержащего количество элементов на странице


class CommentViewViewSet(viewsets.ModelViewSet):
    queryset = CommentView.objects.all()
    serializer_class = CommentViewSerializer
    pagination_class = MyPagination
    ordering = ['created_at']
    ordering_fields = ['-created_at', 'rating']
    allowed_actions = ['create', 'list', 'retrieve']

    def get_permissions(self):
        if self.action == 'destroy' or self.action == 'update':
            permission_classes = [permissions.IsAdminUser]
        else:
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]

    def create(self, request, *args, **kwargs):
        super().create
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
            "message": "Упс! Что-то пошло не так. Разработчики уже работают над исправлением, и вы сможете добавить комментарии снова."
        }
        return Response(responce_400, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['POST'])
    def cleanup_comments(self, request, *args, **kwargs):
        # Выполнить действия по очистке комментариев
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=['PUT'])
    def approve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_approved = True
        if instance.is_approved is True:
            instance.save()
            response_200 = {
                "message": "Comment has been approved and is now available."
            }
            return Response(response_200, status=status.HTTP_200_OK)
        if instance.is_approved is False:
            instance.delete()
            responce_400 = {
                "message": "Комментарий не может быть пройден"
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

class FormQuestionViewSet(TelegramMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = FormQuestion.objects.all()
    serializer_class = FormQuestionSerializer

    def perform_create(self, serializer):
        try:
            super().perform_create(serializer)
            message = f'Форма Главной страницы \nEmail: {serializer.data["email"]}\nMessage: {serializer.data["message"]}'
            self.send_telegram_message(message)
        except APIException:
            return Response({'error': 'Error while sending Telegram message'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class FormBookingViewSet(TelegramMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = FormBooking.objects.all()
    serializer_class = FormBookingSerializer

    def perform_create(self, serializer):
        try:
            super().perform_create(serializer)
            message = f'Форма страницы тура \n' \
                      f'Name: {serializer.data["name"]}\n' \
                      f'Email: {serializer.data["email"]}\n' \
                      f'WhatsApp: {serializer.data["whatsapp"]} \n ' \
                      f'Дата: {serializer.data["date"]}'
            self.send_telegram_message(message)
        except APIException:
            return Response({'error': 'Error while sending Telegram message'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

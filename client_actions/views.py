import os
import requests

from rest_framework import mixins, viewsets, status
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.exceptions import APIException

from .models import (
    CommentView,
    CommentName,
    CommentStar,
    CommentText,
    CommentImage,
    BlogPost,
    FormQuestion,
    FormBooking
)

from .serializers import (
    CommentViewSerializer,
    CommentNameSerializer,
    CommentStarSerializer,
    CommentTextSerializer,
    CommentImageSerializer,
    BlogPostSerializer,
    FormQuestionSerializer,
    FormBookingSerializer
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


class CommentViewViewSet(viewsets.ModelViewSet):
    queryset = CommentView.objects.all()
    serializer_class = CommentViewSerializer
    permission_classes = [IsAdminUser]


class CommentStarViewSet(viewsets.ModelViewSet):
    queryset = CommentStar.objects.all()
    serializer_class = CommentStarSerializer


class CommentImageViewSet(viewsets.ModelViewSet):
    queryset = CommentImage.objects.all()
    serializer_class = CommentImageSerializer


class CommentTextViewSet(viewsets.ModelViewSet):
    queryset = CommentText.objects.all()
    serializer_class = CommentTextSerializer


class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [IsAdminUser]


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

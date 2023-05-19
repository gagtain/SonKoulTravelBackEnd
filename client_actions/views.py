from rest_framework import viewsets, status, permissions
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from datetime import timedelta
from django.utils import timezone
from rest_framework.pagination import PageNumberPagination

from .models import (
    CommentView,
    CommentName,
    CommentStar,
    CommentText,
    CommentImage, ChooseTour,
)

from .serializers import (
    CommentViewSerializer,
    CommentNameSerializer,
    CommentStarSerializer,
    CommentTextSerializer,
    CommentImageSerializer, ChooseTourSerializer,
)


class CommentNameViewSet(viewsets.ModelViewSet):
    queryset = CommentName.objects.all()
    serializer_class = CommentNameSerializer
    allowed_actions = ['create', 'list', 'retrieve']

    def get_permissions(self):
        if self.action in self.allowed_actions:
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]

    def create(self, request, *args, **kwargs):
        serializer = CommentNameSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        serializer = CommentNameSerializer(data=request.data)
        if serializer.is_valid() and IsAdminUser:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        if IsAdminUser:
            instance = self.get_object()
            instance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)


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
        mutable_data = request.data.copy()
        mutable_data["is_approved"] = False
        serializer = CommentViewSerializer(data=mutable_data)
        if serializer.is_valid():
            serializer.save(at_moderation=timezone.now())  # Устанавливаем время модерации
            # Отправка ответа на клиент
            responce_201 = {
                "message": "Спасибо за ваш отзыв! Ваш комментарий был успешно отправлен на модерацию и будет опубликован, как только пройдет проверку."
            }
            return Response(responce_201, status=status.HTTP_201_CREATED) and super().create(request, *args, **kwargs)
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


class CommentStarViewSet(viewsets.ModelViewSet):
    queryset = CommentStar.objects.all()
    serializer_class = CommentStarSerializer
    allowed_actions = ['create', 'list', 'retrieve']

    def get_permissions(self):
        if self.action in self.allowed_actions:
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]

    def create(self, request, *args, **kwargs):
        serializer = CommentStarSerializer(data=request.data)
        if serializer.is_valid() and IsAdminUser:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_403_FORBIDDEN)


class CommentImageViewSet(viewsets.ModelViewSet):
    queryset = CommentImage.objects.all()
    serializer_class = CommentImageSerializer
    allowed_actions = ['create', 'list', 'retrieve']

    def get_permissions(self):
        if self.action in self.allowed_actions:
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]

    def create(self, request, *args, **kwargs):
        serializer = CommentImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            responce_201 = {
                "message": "Изображения успешно добавлены"
            }
            return Response(responce_201, status=status.HTTP_201_CREATED)
        responce_400 = {
            "message": "Ошибка при добавлении изображения или недопустимый формат изображения(Фотографии должны быть"
                       " в формате JPG, PNG)"
        }
        return Response(responce_400, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        serializer = CommentImageSerializer(data=request.data)
        if serializer.is_valid() and IsAdminUser:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        if IsAdminUser:
            instance = self.get_object()
            instance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        responce_403 = {
            "message": "Недостаточно прав! POfse взломать не получится!"
        }
        return Response(responce_403, status=status.HTTP_403_FORBIDDEN)


class ChooseTourViewSet(viewsets.ModelViewSet):
    queryset = ChooseTour.objects.all()
    serializer_class = ChooseTourSerializer
    allowed_actions = ['create', 'list', 'retrieve']

    def get_permissions(self):
        if self.action in self.allowed_actions:
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]

    def create(self, request, *args, **kwargs):
        serializer = ChooseTourSerializer(data=request.data)
        if serializer.is_valid() and IsAdminUser:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_403_FORBIDDEN)

    def update(self, request, *args, **kwargs):
        serializer = ChooseTourSerializer(data=request.data)
        if serializer.is_valid() and IsAdminUser:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_403_FORBIDDEN)

    def destroy(self, request, *args, **kwargs):
        if IsAdminUser:
            instance = self.get_object()
            instance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        responce_403 = {
            "message": "Недостаточно прав! POfse взломать не получится!"
        }
        return Response(responce_403, status=status.HTTP_403_FORBIDDEN)


class CommentTextViewSet(viewsets.ModelViewSet):
    queryset = CommentText.objects.all()
    serializer_class = CommentTextSerializer
    allowed_actions = ['create', 'list', 'retrieve']

    def get_permissions(self):
        if self.action in self.allowed_actions:
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]

    def create(self, request, *args, **kwargs):
        serializer = CommentTextSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        responce_400 = {
            "message": "Ошибка при добавлении текста"
        }
        return Response(responce_400, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        serializer = CommentTextSerializer(data=request.data)
        if serializer.is_valid() and IsAdminUser:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_403_FORBIDDEN)

    def destroy(self, request, *args, **kwargs):
        if IsAdminUser:
            instance = self.get_object()
            instance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        responce_403 = {
            "message": "Недостаточно прав! POfse взломать не получится!"
        }
        return Response(responce_403, status=status.HTTP_403_FORBIDDEN)

from rest_framework import viewsets, status, permissions
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
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
        if self.action in self.allowed_actions:
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]

    def create(self, request, *args, **kwargs):
        serializer = CommentViewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            responce_201 = {
                "message": "Thank you for your feedback! Your review has been successfully submitted and will be published as soon as it passes moderation."
            }
            return Response(responce_201, status=status.HTTP_201_CREATED)
        responce_400 = {
            "message": "oops something happened, the developers will fix it soon and you will be able to add these comments again"
        }
        return Response(responce_400, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        serializer = CommentViewSerializer(data=request.data)
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

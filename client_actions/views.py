from rest_framework import viewsets, status
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from .models import (
    CommentView,
    CommentName,
    CommentStar,
    CommentText,
    CommentImage,
    FormQuestion,
)

from .serializers import (
    CommentViewSerializer,
    CommentNameSerializer,
    CommentStarSerializer,
    CommentTextSerializer,
    CommentImageSerializer,
    FormQuestionSerializer,
)


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
    permission_classes = [IsAdminUser]
    pagination_class = MyPagination
    ordering = ['created_at']
    ordering_fields = ['-created_at', 'rating']


class CommentStarViewSet(viewsets.ModelViewSet):
    queryset = CommentStar.objects.all()
    serializer_class = CommentStarSerializer


class CommentImageViewSet(viewsets.ModelViewSet):
    queryset = CommentImage.objects.all()
    serializer_class = CommentImageSerializer

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


class CommentTextViewSet(viewsets.ModelViewSet):
    queryset = CommentText.objects.all()
    serializer_class = CommentTextSerializer


class FormQuestionViewSet(viewsets.GenericViewSet):
    queryset = FormQuestion.objects.all()
    serializer_class = FormQuestionSerializer

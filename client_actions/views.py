import requests
from rest_framework import generics, status
from rest_framework.permissions import IsAdminUser, IsUserAuthor
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT
from rest_framework.generics import ListCreateAPIView


from .models import (
    CommentView,
    CommentName,
    CommentStar, CommentText,
    CommentImage,
    BlogPost,
    FormQuestion
)

from .serializers import (
    CommentViewSerializer,
    CommentNameSerializer,
    CommentStarSerializer,
    CommentTextSerializer,
    CommentImageSerializer,
    BlogPostSerializer,
    FormQuestionSerializer
)

symbols = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}


class CommentNameView(ListCreateAPIView):
    queryset = CommentName.objects.all()
    serializer_class = CommentNameSerializer


class CommentViewList(APIView):
    queryset = CommentView.objects.all()
    serializer_class = CommentViewSerializer

    def post(self, request):
        serializer = CommentViewSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=HTTP_201_CREATED)


class CommentViewRetrieveUpdateDestroy(APIView):
    queryset = CommentView.objects.all()
    serializer_class = CommentViewSerializer
    permission_classes = [IsAdminUser]

    def put(self, request, pk):
        serializer = CommentViewSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=HTTP_201_CREATED)

    def delete(self, request, pk):
        post = CommentView.objects.get(pk=pk)
        post.delete()
        return Response(status=HTTP_204_NO_CONTENT)

    def get(self, request, pk):
        post = CommentView.objects.get(pk=pk)
        serializer = CommentViewSerializer(post)
        return Response(serializer.data)


class CommentStarView(ListCreateAPIView):
    queryset = CommentStar.objects.all()
    serializer_class = CommentStarSerializer


class CommentImageView(ListCreateAPIView):
    queryset = CommentImage.objects.all()
    serializer_class = CommentImageSerializer


class CommentTextView(ListCreateAPIView):
    queryset = CommentText.objects.all()
    serializer_class = CommentTextSerializer


class BlogPostView(ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [IsAdminUser]


class BlogPostRetrieveUpdateDestroy(APIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [IsAdminUser]

    def put(self, request, pk):
        serializer = BlogPostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=HTTP_201_CREATED)

    def delete(self, request, pk):
        post = BlogPost.objects.get(pk=pk)
        post.delete()
        return Response(status=HTTP_204_NO_CONTENT)

    def get(self, request, pk):
        post = BlogPost.objects.get(pk=pk)
        serializer = BlogPostSerializer(post)
        return Response(serializer.data)


class FormQuestionView(generics.CreateAPIView):
    queryset = FormQuestion.objects.all()
    serializer_class = FormQuestionSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        # Отправка данных в телеграмм
        bot_token = '5964377497:AAEXxcJ745bQpNUpB2neHIjMMkf0IBF5mn4'
        chat_id = '860389338'
        message = f'Name: {serializer.data["name"]}\nEmail: {serializer.data["email"]}\nMessage: {serializer.data["message"]}'
        url = f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={message}'
        requests.post(url)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


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


class FormQuestionView(ListCreateAPIView):
    queryset = FormQuestion.objects.all()
    serializer_class = FormQuestionSerializer

from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_201_CREATED, HTTP_204_NO_CONTENT
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

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = BlogPostSerializer(instance=instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=HTTP_201_CREATED)


class FormQuestionView(ListCreateAPIView):
    queryset = FormQuestion.objects.all()
    serializer_class = FormQuestionSerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=HTTP_204_NO_CONTENT)

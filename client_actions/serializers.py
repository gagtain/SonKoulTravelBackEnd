from rest_framework import serializers, status, request
from rest_framework.response import Response

from .models import (
    CommentText,
    CommentStar,
    CommentName,
    CommentView,
    CommentImage,
    BlogPost,
    FormQuestion
)


class CommentTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentText
        fields = '__all__'

        read_only_fields = ('id',)


class CommentStarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentStar
        fields = 'name', 'stars'

        read_only_fields = ('id',)


class CommentNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentName
        fields = '__all__'

        read_only_fields = ('id',)


class CommentImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentImage
        fields = '__all__'

        read_only_fields = ('id',)


class CommentViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentView
        fields = '__all__'

        read_only_fields = ('id',)


def is_admin(instance):
    admin = instance.user.is_superuser
    if admin:
        return True


class BlogPostSerializer(serializers.ModelSerializer):
    date = serializers.DateTimeField(format='%H:%M:%S', allow_null=True, required=False)

    class Meta:
        model = BlogPost
        fields = 'title image text date'.split()

        read_only_fields = ('id', 'date')


class FormQuestionSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(format='%H:%M:%S', allow_null=True, required=False)

    class Meta:
        model = FormQuestion
        fields = '__all__'

        read_only_fields = ('id', 'created')

        extra_kwargs = {
            'created': {'read_only': True}
        }

from django.core.validators import MaxValueValidator
from rest_framework import serializers

from .models import (
    CommentText,
    CommentStar,
    CommentName,
    CommentView,
    CommentImage,
    BlogPost,
    FormQuestion,
    FormBooking,
)
from client_actions.fields import WEBPField


class BaseSerializer(serializers.ModelSerializer):
    read_only_fields = ('id',)

    def get_fields(self):
        fields = super().get_fields()
        if self.instance and self.context['request'].user.is_superuser:
            return fields
        return {
            k: v for k, v in fields.items() if not getattr(v, 'write_only', False)
        }


class CommentTextSerializer(BaseSerializer):
    class Meta:
        model = CommentText
        fields = '__all__'


class CommentStarSerializer(BaseSerializer):
    class Meta:
        model = CommentStar
        fields = '__all__'


class CommentNameSerializer(BaseSerializer):
    class Meta:
        model = CommentName
        fields = '__all__'


class CommentImageSerializer(BaseSerializer):
    class Meta:
        model = CommentImage
        fields = '__all__'


class CommentViewSerializer(BaseSerializer):
    class Meta:
        model = CommentView
        fields = '__all__'


class BlogPostSerializer(BaseSerializer):
    date = serializers.DateTimeField(format='%H:%M:%S', allow_null=True, required=False)
    image = serializers.ListField(
        child=serializers.ImageField(),
        required=False,
        allow_empty=True,
    )

    class Meta:
        model = BlogPost
        fields = 'title image text date'.split()


class FormQuestionSerializer(BaseSerializer):
    created = serializers.DateTimeField(format='%H:%M:%S', allow_null=True, required=False)

    class Meta:
        model = FormQuestion
        fields = '__all__'

        extra_kwargs = {
            'created': {'read_only': True},
        }


class FormBookingSerializer(BaseSerializer):
    date = serializers.DateTimeField(format='%H:%M:%S', allow_null=True)

    class Meta:
        model = FormBooking
        fields = '__all__'

        extra_kwargs = {
            'id': {'read_only': True},
        }

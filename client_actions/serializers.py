from rest_framework import serializers

from tour.models import TourAdd
from .models import (
    CommentText,
    CommentStar,
    CommentName,
    CommentView,
    CommentImage, ChooseTour,
)


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


class ChooseTourSerializer(serializers.ModelSerializer):

    class Meta:
        model = ChooseTour
        fields = '__all__'

    def get_tour(self, obj):
        return obj.tour.name


class CommentViewSerializer(BaseSerializer):
    class Meta:
        model = CommentView
        fields = 'stars name text image image_two image_three image_four tour date'.split()

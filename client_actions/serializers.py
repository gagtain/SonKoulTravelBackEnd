from rest_framework import serializers

from .models import CommentView


class BaseSerializer(serializers.ModelSerializer):
    read_only_fields = ('id',)

class CommentViewSerializer(BaseSerializer):
    date = serializers.DateTimeField(read_only=True, format='%Y-%m-%d')

    class Meta:
        model = CommentView
        fields = 'id stars name text image image_two image_three image_four tour date is_approved'.split()
        read_only_fields = ('id',)

        extra_kwargs = {
            "tour": {"required": False},
            "id": {"required": False},
        }

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['tour'] = instance.tour.name
        return data

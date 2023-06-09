from rest_framework import serializers

from .models import CommentView, Photo
from .compress_image import compress_image


class BaseSerializer(serializers.ModelSerializer):
    read_only_fields = ('id',)


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ['photo']

    def create(self, validated_data):
        photo = Photo.objects.create(**validated_data)
        compress_image(photo)
        return photo


class CommentViewSerializer(serializers.ModelSerializer):

    class Meta:
        model = CommentView
        fields = ['id', 'stars', 'name', 'text', 'photos', 'tour', 'date', 'is_approved']
        read_only_fields = ('id', 'date', 'is_approved')
        extra_kwargs = {
            "tour": {"required": False},
            "id": {"required": False}

        }

    def create(self, validated_data):
        photos_data = validated_data.pop('photos')
        comment = CommentView.objects.create(**validated_data)
        for photo_data in photos_data:
            Photo.objects.create(comment=comment, **photo_data)
        return comment

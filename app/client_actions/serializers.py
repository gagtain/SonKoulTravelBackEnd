from rest_framework import serializers

from .compress_image import compress_image
from .models import CommentView, PhotoComment
from tour.serializers import TourAddSerializer

import base64


class PhotoSerializer(serializers.ModelSerializer):
    photo = serializers.ImageField(required=False)

    class Meta:
        model = PhotoComment
        fields = ['id', 'photo', 'comment']


class CommentViewSerializer(serializers.ModelSerializer):
    upload_images = PhotoSerializer(many=True, required=False)

    class Meta:
        model = CommentView
        fields = ['id', 'stars', 'name', 'text', 'photos', 'tour', 'date', 'is_approved', 'upload_images']
        read_only_fields = ('id', 'date', 'is_approved', 'photos')
        extra_kwargs = {
            "tour": {"required": False},
            "id": {"required": False}
        }

    def to_representation(self, instance):
        host = self.context['request'].get_host() if self.context['request'].get_host() else None
        data = super().to_representation(instance)
        tour_name = instance.tour.name if instance.tour else None
        data['tour'] = tour_name
        data['photos'] = [f"{host}{photo.photo.url}" for photo in instance.photos.all()]

        return data

    def create(self, validated_data):
        photos_data = validated_data.pop('upload_images', [])
        comment = CommentView.objects.create(**validated_data)
        for photo_data in photos_data:
            photo = PhotoComment.objects.create(comment=comment, **photo_data)
        return comment

from rest_framework import serializers

from .models import CommentView, Photo


class PhotoSerializer(serializers.ModelSerializer):
    photo = serializers.FileField()

    class Meta:
        ref_name = "CommentsPhoto"
        model = Photo
        fields = '__all__'

    def create(self, validated_data):
        return Photo.objects.create(**validated_data)


class CommentViewSerializer(serializers.ModelSerializer):
    photos = PhotoSerializer(many=True, required=False)

    class Meta:
        model = CommentView
        fields = ['id', 'stars', 'name', 'text', 'photos', 'tour', 'date', 'is_approved']
        read_only_fields = ('id', 'date', 'is_approved')
        extra_kwargs = {
            "tour": {"required": False},
            "id": {"required": False}
        }

    def create(self, validated_data):
        photos_data = validated_data.pop('photos', [])
        comment = CommentView.objects.create(**validated_data)
        for photo_data in photos_data:
            Photo.objects.create(comment=comment, **photo_data)
        return comment

    def to_representation(self, instance):
        data = super(CommentViewSerializer, self).to_representation(instance)
        data['tour'] = instance.tour.name
        data['photos'] = PhotoSerializer(instance.photos.all(), many=True).data
        return data

from rest_framework import serializers

from .models import CommentView, Photo


class PhotoSerializer(serializers.ModelSerializer):
    photo = serializers.FileField()

    class Meta:
        ref_name = "CommentsPhoto"
        model = Photo
        fields = '__all__'

<<<<<<< HEAD
    def create(self, validated_data):
        return Photo.objects.create(**validated_data)

=======
>>>>>>> 4716c94fb53bd60f6cb2913688b43c44fa81afcf

class CommentViewSerializer(serializers.ModelSerializer):
    photos = PhotoSerializer(many=True, required=False, read_only=True)
    upload_images = serializers.ListField(
        child = serializers.FileField(max_length = 1000000, allow_empty_file = False, use_url = False),
        write_only = True
    )

    class Meta:
        model = CommentView
        fields = ['id', 'stars', 'name', 'text', 'photos', 'tour', 'date', 'is_approved', 'upload_images']
        read_only_fields = ('id', 'date', 'is_approved', 'photos')
        extra_kwargs = {
            "tour": {"required": False},
            "id": {"required": False}
        }

    def create(self, validated_data):
        photos_data = validated_data.pop('upload_images', [])
        print(f"adasda={photos_data}")
        comment = CommentView.objects.create(**validated_data)
        for photo_data in photos_data:
            photo_data = compress_image(photo_data)
            print(photo_data)
            Photo.objects.create(comment=comment, photo=photo_data)
        return comment

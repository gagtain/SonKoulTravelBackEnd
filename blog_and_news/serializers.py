from rest_framework import serializers

from .models import BlogNews


class BlogSerializer(serializers.ModelSerializer):
    date_posted = serializers.DateTimeField(format='%d-%m-%y')

    class Meta:
        model = BlogNews
        fields = 'title category date_posted image content'.split()

from rest_framework import serializers

from .models import BlogNews, Body


class BlogSerializer(serializers.ModelSerializer):
    date_posted = serializers.DateTimeField(format='%d-%m-%y')

    class Meta:
        model = BlogNews
        fields = 'title category date_posted image'.split()


class BodySerializer(serializers.ModelSerializer):

    class Meta:
        model = Body
        fields = '__all__'

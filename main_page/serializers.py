from rest_framework import serializers

from .models import FormQuestion


class FormQuestionSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True, format='%d-%m-%Y')

    class Meta:
        model = FormQuestion
        fields = '__all__'

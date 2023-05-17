import re
from datetime import datetime

from rest_framework import serializers
from rest_framework.response import Response

from .models import (
    TourAdd,
    TourProgram,
    Price,
    Tips,
    Photo,
    TourDates,
    BookingPrivateTour,
    BookingGroupTour, PriceDetails, TourDate,
)


class TourAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourAdd
        fields = '__all__'


class TourProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourProgram
        fields = '__all__'


class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = '__all__'


class TipsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tips
        fields = '__all__'


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'


class TourDatesSerializer(serializers.ModelSerializer):

    class Meta:
        model = TourDates
        fields = '__all__'


class BookingPrivateTourSerializer(serializers.ModelSerializer):

    class Meta:
        model = BookingPrivateTour
        fields = '__all__'


class BookingGroupTourSerializer(serializers.ModelSerializer):
    date_str = serializers.SerializerMethodField(read_only=True, default='None')
    # email_or_whatsapp = serializers.CharField()

    class Meta:
        model = BookingGroupTour
        fields = 'id name email_or_whatsapp date date_str'.split()

    def get_date_str(self, instance):
        return str(instance.date)

    # def validate_email_or_whatsapp(self, value):
    #     if not value:
    #         raise serializers.ValidationError("Поле name не может быть пустым")
    #
    #         # Проверяем, что значение содержит только буквы
    #     if not re.match(r'^[a-zA-Z]+$', value):
    #         raise serializers.ValidationError("Поле name должно содержать только буквы")
    #
    #     return value

class PriceDetailsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceDetails
        fields = 'person per_person'.split()


class PriceDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = PriceDetails
        fields = '__all__'





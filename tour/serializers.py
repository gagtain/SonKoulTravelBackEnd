import re
from datetime import datetime

from rest_framework import serializers

from .models import (
    TourAdd,
    TourProgram,
    Price,
    Tips,
    Photo,
    TourDates,
    BookingPrivateTour,
    BookingGroupTour, PriceDetails,
)


class TourAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourAdd
        fields = '__all__'


class TourProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourProgram
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['tour'] = instance.tour.name
        return data


class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = (
            'id',
            'price_includes',
            'price_includes_2',
            'price_includes_3',
            'price_includes_4',
            'price_includes_5',
            'price_includes_6',
            'price_includes_7',
            'price_includes_8',
            'price_includes_9',
            'price_includes_10',
            'price_not_includes',
            'price_not_includes_2',
            'price_not_includes_3',
            'price_not_includes_4',
            'price_not_includes_5',
            'price_not_includes_6',
            'price_not_includes_7',
            'price_not_includes_8',
            'price_not_includes_9',
            'price_not_includes_10',
        )

    def to_representation(self, instance):
        data = super().to_representation(instance)
        for key, value in data.items():
            if not value:
                data[key] = None
        return data


class TipsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tips
        fields = \
            [
                "tittle",
                "what_to_bring",
                "what_to_bring_2",
                "what_to_bring_3",
                "what_to_bring_4",
                "what_to_bring_5",
                "what_to_bring_6",
                "what_to_bring_7",
                "what_to_bring_8",
                "what_to_bring_9",
                "what_to_bring_10",
                "what_to_bring_11",
                "what_to_bring_12",
                "what_to_bring_13",
                "what_to_bring_14",
                "what_to_bring_15",
                "tittle_2",
                "description"
            ]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        for key, value in data.items():
            if not value:
                data[key] = None
        return data


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['tour'] = instance.tour.name
        return data


class TourDatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourDates
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['tour'] = instance.tour.name
        return data


class BookingPrivateTourSerializer(serializers.ModelSerializer):
    date = serializers.DateTimeField(format="%d.%m.%Y")
    date_up_to = serializers.DateTimeField(format="%d.%m.%Y")

    class Meta:
        model = BookingPrivateTour
        fields = 'id name email_or_whatsapp date date_up_to tour'.split()

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['tour'] = instance.tour.name
        return data




class BookingGroupTourSerializer(serializers.ModelSerializer):
    date_str = serializers.SerializerMethodField(read_only=True, default='None')

    # email_or_whatsapp = serializers.CharField()

    class Meta:
        model = BookingGroupTour
        fields = 'name email_or_whatsapp date date_str tour'.split()

    def get_date_str(self, instance):
        return str(instance.date)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['tour'] = instance.tour.name
        return data

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
        fields = 'id person per_person tour'.split()


class PriceDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceDetails
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['tour'] = instance.tour.name
        return data

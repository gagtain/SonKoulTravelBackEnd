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
    BookingGroupTour
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
    "tittle_2" ,
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


class TourDatesSerializer(serializers.ModelSerializer):
    date = serializers.DateField(format="%d.%m.%y")

    class Meta:
        model = TourDates
        fields = ('date',)


class BookingPrivateTourSerializer(serializers.ModelSerializer):
    date = TourDatesSerializer(read_only=True)

    class Meta:
        model = BookingPrivateTour
        fields = ('name', 'email_or_whatsapp', 'date')


class BookingGroupTourSerializer(serializers.ModelSerializer):
    date = TourDatesSerializer(required=False)

    class Meta:
        model = BookingGroupTour
        fields = ('name', 'email_or_whatsapp', 'date')

    def create(self, validated_data):
        date = validated_data.pop('date', None)
        if date is not None:
            validated_data['date'] = date.date()
        return super().create(validated_data)

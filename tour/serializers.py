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

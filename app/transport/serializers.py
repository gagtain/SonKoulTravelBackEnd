from rest_framework import serializers

from .models import (
    CarRental,
    Taxi
)


class CarRentalSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarRental
        fields = '__all__'


class TaxiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Taxi
        fields = '__all__'

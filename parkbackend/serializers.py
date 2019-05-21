from rest_framework import serializers
from .models import *


class CAddCityListSerializer(serializers.ModelSerializer):

    class Meta:
        model = ParkingLot
        fields = ('mg_id', 'name')

    mg_id = serializers.SerializerMethodField('mg_id_field')

    def mg_id_field(self, obj):
        return obj.id

    name = serializers.SerializerMethodField('name_field')

    def name_field(self, obj):
        return obj.parking_name


class ChargeStandardSerializer(serializers.ModelSerializer):

    class Meta:
        model = ChargeStandard
        fields = ('parking', 'car_type', 'day_money', 'night_money', 'all_day_money', 'time_unit', 'start_time', 'end_time')

        parking = serializers.SerializerMethodField('parking_field')
        def parking_field(self, obj):
            return obj.parking.parking_name


from rest_framework import serializers
from .models import *

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

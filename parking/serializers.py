from rest_framework import serializers
from .models import *
from userinfo.serializers import *
from backend.models import *

class ParkingSerializer(serializers.ModelSerializer):

    # customer = UserInfoSerializer(many=False, read_only=True)

    class Meta:
        model = ParkingLot
        fields = ('mg_id', 'longitude', 'latitude', 'total', 'area', 'address', 'lo', 'la', 'markerAddress', 'marker', 'occupy', 'leftpos')

    mg_id = serializers.SerializerMethodField('id_field')

    def id_field(self, obj):
        return obj.id

    total = serializers.SerializerMethodField('total_field')

    def total_field(self, obj):
        return obj.total_number

    area = serializers.SerializerMethodField('area_field')

    def area_field(self, obj):
        ads = obj.province+obj.city+obj.area
        return ads

    lo = serializers.SerializerMethodField('lo_field')

    def lo_field(self, obj):
        return obj.longitude

    la = serializers.SerializerMethodField('la_field')

    def la_field(self, obj):
        return obj.latitude

    markerAddress = serializers.SerializerMethodField('markerAddress_field')

    def markerAddress_field(self, obj):
        ads = obj.province + obj.city + obj.area + obj.address
        return ads

    marker = serializers.SerializerMethodField('marker_field')

    def marker_field(self, obj):
        return ""

    occupy = serializers.SerializerMethodField('occupy_field')

    def occupy_field(self, obj):
        return 0

    leftpos = serializers.SerializerMethodField('leftpos_field')

    def leftpos_field(self, obj):
        return obj.remain_number


class LastParkingSerializer(serializers.ModelSerializer):

    class Meta:
        model = ParkingRecord
        fields = ('name', 'number', 'mg_id')

    name = serializers.SerializerMethodField('name_field')

    def name_field(self, obj):
        return obj.parking.parking_name

    number = serializers.SerializerMethodField('number_field')

    def number_field(self, obj):
        return 1

    mg_id = serializers.SerializerMethodField('id_field')

    def id_field(self, obj):
        return obj.id


class ParkingDetailSerializer(serializers.ModelSerializer):

    # customer = UserInfoSerializer(many=False, read_only=True)

    class Meta:
        model = ParkingLot
        fields = ('name', 'address', 'total', 'longitude', 'latitude', 'logo', 'leftpos', 'types')

    name = serializers.SerializerMethodField('name_field')

    def name_field(self, obj):
        return obj.parking_name

    address = serializers.SerializerMethodField('address_field')

    def address_field(self, obj):
        ads = obj.province + obj.city + obj.area + obj.address
        return ads

    total = serializers.SerializerMethodField('total_field')

    def total_field(self, obj):
        return obj.total_number

    logo = serializers.SerializerMethodField('logo_field')

    def logo_field(self, obj):
        return 'logo'

    leftpos = serializers.SerializerMethodField('leftpos_field')

    def leftpos_field(self, obj):
        return obj.remain_number

    types = serializers.SerializerMethodField('type_field')

    def type_field(self, obj):
        if obj.parking_type == 0:
            return u'室内'
        elif obj.parking_type == 1:
            return u'室外'




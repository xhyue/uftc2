from rest_framework import serializers
from .models import *
from userinfo.serializers import *
# class CollegeSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = College
#         fields = ('id', 'college_id', 'college_name')
#
#
# class MajorSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Major
#         fields = ('id', 'major_id', 'major_name', 'college')
#
#     college = serializers.SerializerMethodField('college_field')
#     def college_field(self, obj):
#         return obj.college.college_name
#

class PaymentRecordSerializer(serializers.ModelSerializer):

    # customer = UserInfoSerializer(many=False, read_only=True)

    class Meta:
        model = PaymentRecord
        fields = ('id',  'reason', 'parking', 'account', 'duration', 'flag')

    reason = serializers.SerializerMethodField('reason_field')

    def reason_field(self, obj):
        return '停车费'

    parking = serializers.SerializerMethodField('parking_field')

    def parking_field(self, obj):
        return obj.parking.parking_name

    account = serializers.SerializerMethodField('payment_money_field')

    def payment_money_field(self, obj):
        return obj.payment_money

    duration = serializers.SerializerMethodField('payment_date_field')

    def payment_date_field(self, obj):
        return obj.payment_date

    flag = serializers.SerializerMethodField('flag_field')

    def flag_field(self, obj):
        return 1


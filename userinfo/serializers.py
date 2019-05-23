from rest_framework import serializers
from .models import *

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

class UserInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserInfo
        fields = ('customer_name','nickname','avatar','gender','birth','openid')

class CarInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = CarInfo
        fields = ('id', 'plate', 'brand', 'version', 'type', 'displacement', 'carImg')

    carImg = serializers.SerializerMethodField('carImg_field')

    def carImg_field(self, obj):
        drive_license = str(obj.drive_license)
        return drive_license

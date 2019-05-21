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

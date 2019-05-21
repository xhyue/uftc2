from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'^addparkingcity', CustomerAddParking.as_view(), name='addpcity_view'),
]
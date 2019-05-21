from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'chargestandard', ChargeStandardView.as_view(), name='charge_standard'),
    url(r'^addparkingcity', CustomerAddParking.as_view(), name='addpcity_view'),
]
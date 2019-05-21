from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'parkingrecord', ParkingRecordView.as_view(), name='parking_record')

]
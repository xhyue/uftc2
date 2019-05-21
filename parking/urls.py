from django.conf.urls import url
from django.views.generic import TemplateView
from .views import *

urlpatterns = [
    url(r'^index', IndexView.as_view(), name='index_view'),
    url(r'^used', UsedView.as_view(), name='usedlist_view'),
    url(r'^getroute', GetRoute.as_view(), name='getroute_view'),
    url(r'^detail', ParkingDetail.as_view(), name='detail_view'),
    url(r'^parksearch', SearchParking.as_view(), name='parksearch_view'),
]
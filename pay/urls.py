from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'^myMoneybag', PayList.as_view(), name='pay_view'),
    url(r'^alipaytest', ChargePay.as_view(), name='charge_view'),
    # url(r'^charge', ChargePay.as_view(), name='charge_view'),
    url(r'^confirmcharge', AliConfirmCharge.as_view(), name='confirmcharge_view'),
]
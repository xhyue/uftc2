from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^myMoneybag', PayList.as_view(), name='pay_view'),
    url(r'^alipaytest', Alipay.as_view(), name='alipaytest_view'),
]
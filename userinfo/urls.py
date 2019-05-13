from django.conf.urls import url
from .views import *
urlpatterns = [
    url(r'^verifycode', VerificationCode.as_view(), name='verify_code'),
    url(r'^cuslogin', CustomerLogin.as_view(), name='customer_login'),
    url(r'^cusinfo', CustomerInfo.as_view(), name='customer_info'),

]
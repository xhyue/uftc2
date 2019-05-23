from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'verifycode', VerifyCodeView.as_view(), name='verify_code'),
    url(r'phonelogin', PhoneLogin.as_view(), name='phone_login'),
    url(r'^cusinfo', CustomerInfo.as_view(), name='customer_info'),
    url(r'^selfcar', SelfCar.as_view(), name='selfcar_info'),


]
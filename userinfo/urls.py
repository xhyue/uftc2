from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'verifycode', VerifyCodeView.as_view(), name='verify_code'),
    url(r'phonelogin', PhoneLogin.as_view(), name='phone_login'),

]
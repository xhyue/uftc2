from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'pc/login/$', PCAdminLogin.as_view(), name='pc_login'),
]
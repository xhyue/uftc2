from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^parkList', parkList.as_view(), name='park_view'),

]
from django.conf.urls import url
from django.views.generic import TemplateView
from .views import *

urlpatterns = [
    url(r'chargestandard', ChargeStandardView.as_view(), name='charge_standard')

]
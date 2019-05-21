# restful API
from rest_framework.views import APIView

# django
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist

# selfproject
from .serializers import *
from .models import *

# base
import logging


logger = logging.getLogger('sourceDns.webdns.views')

# Create your views here.

class ChargeStandardView(APIView):
    def get(self, request):
        parking_id = request.GET.get('pid', "")
        car_type = request.GET.get('car_type', "")
        if parking_id == "" or car_type == "":
            code = 1001
            data = ""
            msg = "参数不能为空"
            return JsonResponse({"code": code, "data": data, "msg": msg})
        chargestandard = ChargeStandard.objects.filter(parking=parking_id, car_type=car_type)
        if not chargestandard:
            code = 1001
            data = ""
            msg = "未查询到该停车场收费标准"
            return JsonResponse({"code": code, "data": data, "msg": msg})
        chargestandardata = ChargeStandardSerializer(chargestandard, many=True)
        data = chargestandardata.data
        code = 1000
        msg = ""
        return JsonResponse({"code": code, "data": data, "msg": msg})






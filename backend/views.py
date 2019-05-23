# restful API
from rest_framework.views import APIView

# selfproject
from backend.models import *
from userinfo.models import *
from parking.models import *
from pay.models import *

# django
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.core.cache import cache
from django.http import JsonResponse

#base
import os
import datetime
import time

# Create your views here.

class ParkingRecordView(APIView):
    def post(self, request):
        uid = request.POST.get("uid", "")
        pid = request.POST.get("pid", "")
        number_plate = request.POST.get("number_plate", "")
        entry_time = request.POST.get("entry_time", "")
        exit_time = request.POST.get("exit_time", "")
        file1 = request.FILES.get("file1", "")
        file2 = request.FILES.get("file2", "")
        total_time = request.POST.get("total_time", "")
        total_money = request.POST.get("total_money", "")
        payment_mode_id = request.POST.get("payment_mode_id", "")
        entry_time_str = entry_time[0:4]+entry_time[5:7]+entry_time[8:10]+entry_time[11:13]+entry_time[14:16]+entry_time[17:19]
        entry_time_db = datetime.datetime.strptime(entry_time_str, "%Y%m%d%H%M%S")
        exit_time_str = exit_time[0:4]+exit_time[5:7]+exit_time[8:10]+exit_time[11:13]+exit_time[14:16]+exit_time[17:19]
        exit_time_db = datetime.datetime.strptime(exit_time_str, "%Y%m%d%H%M%S")
        customer = UserInfo.objects.filter(id=uid)
        parking_lot = ParkingLot.objects.filter(id=pid)
        bank = Bank.objects.filter(id=payment_mode_id)
        ParkingRecord.objects.create(customer=customer[0], parking=parking_lot[0], number_plate=number_plate,
                                     entry_time=entry_time_db, exit_time=exit_time_db, entry_picture=file1,
                                     exit_picture=file2, total_time=total_time, total_money=total_money,
                                     payment_mode=bank[0])
        code = 1000
        data = ""
        msg = "ok"
        return JsonResponse({"code": code, "data": data, "msg": msg})





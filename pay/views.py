# django
from django.http import JsonResponse

from rest_framework.views import APIView

from .models import *
from .serializers import *
from .alipay import *
# Create your views here.


class PayList(APIView):

    def post(self, request):
        uid = request.POST.get('uid', '')
        page = request.POST.get('page', 1)
        token = request.POST.get('token', '')
        from_page = (int(page)-1)*10+1
        to_page = int(page)*10
        data = {}
        maxPage = PaymentRecord.objects.filter(customer_id=1).count()
        if maxPage > 1:
            pay_list = PaymentRecord.objects.filter(customer_id=uid, id__range=(from_page, to_page))
        else:
            pay_list = PaymentRecord.objects.filter(customer_id=uid)
        pay_data = PaymentRecordSerializer(pay_list, many=True)
        money = Wallet.objects.filter(customer_id=uid)[0].money
        lists = pay_data.data
        code = 1000
        data['list'] = lists
        data['maxPage'] = maxPage
        data['money'] = money
        msg = '我的钱包数据获取成功'
        return JsonResponse({"code": code, "data": data, "msg": msg})

class Alipay(APIView):

    def post(self,request):
        # user_id = request.POST.get('user_id')
        money = request.POST.get('money')
        test = recharge(money)
        data = {}
        print(test)
        code = 1000
        data['test'] = test
        msg = '我的钱包数据获取成功'
        return JsonResponse({"code": code, "data": data, "msg": msg})

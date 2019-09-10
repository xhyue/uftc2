# django
from django.http import JsonResponse, HttpResponse
from django.core.exceptions import ObjectDoesNotExist

from rest_framework.views import APIView

from .models import *
from .serializers import *
from .alipaygf import AlipayAPI

import datetime
import logging

logger = logging.getLogger('sourceDns.webdns.views')


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


class ChargePay(APIView):

    def post(self,request):
        user_id = '3'
        # user_id = request.POST.get('user_id',1)
        subject = '充值'
        # total_amount = request.POST.get('money','0.00')
        total_amount = 0.01
        if len(user_id) < 6:
            s_trade_no = '0'*(6-len(user_id))+user_id
        else:
            s_trade_no = user_id
        out_trade_no = datetime.datetime.now().strftime("%Y%m%d%H%M%S")+s_trade_no
        charge_time = str(datetime.datetime.now())
        body={}
        body['charge']=charge_time
        body['subject']=subject
        body['total_amount']=total_amount
        body = str(body)
        try:
            recharge = RechargeRecord.objects.create(customer_id=user_id, out_trade_no=out_trade_no, charge_mode_id=1, charge_money=total_amount, charge_date=charge_time, pay_status=2)
        except ObjectDoesNotExist as e:
            logger.error(e)
        data = AlipayAPI().TradeAppPay(body, subject, out_trade_no, total_amount)
        return HttpResponse(data)


class AliConfirmCharge(APIView):

    def post(self,request):
        result = request.POST.dict()
        if AlipayAPI().CheckAppPay(result):
            print("@@@@@:",result)
            print("@@@@@:",result['out_trade_no'])
            return HttpResponse('success')
        else:
            return HttpResponse('')

        # trade_no #'2019061422001490220527923878'支付宝交易号
        # trade_status #TRADE_SUCCESS交易状态WAIT_BUYER_PAY	交易创建，等待买家付款
                                        # TRADE_CLOSED	未付款交易超时关闭，或支付完成后全额退款
                                        # TRADE_SUCCESS	交易支付成功
                                        # TRADE_FINISHED	交易结束，不可退款
        # notify_type #trade_status_sync通知类型
        # subject #充值订单标题
        # charset #UTF-8编码格式
        # gmt_create #2019-06-14 11:41:05交易创建时间
        # receipt_amount #0.01
        # fund_bill_list #['[{"amount":"0.01","fundChannel":"ALIPAYACCOUNT"}]'],
        # buyer_id #2088522675590225
        # sign #PhmIeNB....
        # notify_id #2019061400222114106090220593748175通知校验ID
        # gmt_payment #2019-06-14 11:41:06交易付款时间
        # notify_time #2019-06-14 11:41:07通知时间
        # version #1.0接口版本
        # auth_app_id #2018080360972019
        # point_amount #0.00集分宝金额
        # body #"{'total_amount': 0.01, 'charge': datetime.datetime(2019, 6, 14, 3, 41, 0, 422270), 'subject': '充值'}"],商品描述
        # seller_id #2088902702939870卖家支付宝用户号
        # app_id #2018080360972019支付宝分配给开发者的应用Id
        # buyer_logon_id #135****6483买家支付宝用户号
        # invoice_amount #0.01开票金额
        # sign_type #RSA2签名类型
        # out_trade_no #20190614034100000003商户订单号
        # buyer_pay_amount #0.01付款金额
        # seller_email #gukudlq@126.com卖家支付宝账号
        # total_amount #0.01订单金额



        return HttpResponse()


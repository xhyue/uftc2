
# restful API
from rest_framework.views import APIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_jwt.settings import api_settings
from rest_framework_jwt.utils import jwt_decode_handler

# django
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist

# selfproject
from .verifycode import *
from .models import *
from pay.models import *

# base
import logging
import re
import random
# import jwt

# Create your views here.
logger = logging.getLogger('sourceDns.webdns.views')

class VerifyCodeView(APIView):
    def post(self, request):
        phone = request.POST.get("phone", "")
        if re.findall('^1((3[\d])|(4[75])|(5[^3|4])|(66)|(7[013678])|(8[\d])|(9[89]))\d{8}$', phone):
            code = 1000
            data = ""
            msg = "正确手机号"
        else:
            code = 1002
            data = ""
            msg = "手机号不正确，请重新输入"
            return JsonResponse({"code": code, "data": data, "msg": msg})
        result = SendVerifyCode(phone)
        result_dict = json.loads(result._SendVerifyCode__sendsms)
        try:
            sendsms = result_dict['sendsms']
        except KeyError as e:
            logger.error(e)
        if sendsms == "success":
            code = 1000
            data = ""
            msg = "验证码发送成功"
            verify = result_dict['verifycode']
            request.session['phone'] = phone
            request.session['verify'] = verify
        else:
            code = 1001
            data = ""
            msg = "发送失败"
        return JsonResponse({"code": code, "data": data, "msg": msg})


class PhoneLogin(APIView):
    def post(self, request):
        uphone = request.POST.get("phone", "")
        verify_code = request.POST.get("code", "")
        # phone_session = request.session.get('phone')
        # code_session = request.session.get('verify')
        # if uphone != phone_session or verify_code != code_session:
        #     code = 1002
        #     data = ""
        #     msg = "验证码有误"
        #     return JsonResponse({"code": code, "data": data, "msg": msg})
        customer = UserInfo.objects.filter(customer_name=uphone)
        if customer:
            code = 1000
            msg = "登录成功"
            # jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
            # jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
            # logininfo = jwt_payload_handler(customer)
            # token = jwt_encode_handler(logininfo)
            data = {}
            data['uid'] = customer[0].id
            data['avatar'] = str(customer[0].avatar)
            data['sex'] = customer[0].gender
            data['username'] = customer[0].customer_name
            # data['token'] = token
        else:
            num = ""
            for i in range(6):
                ch = chr(random.randrange(ord('0'), ord('9') + 1))
                num += ch
            nicknamelistf = ['爱吃', '讨厌', '咬着', '手拿']
            nicknamelists = ['榴莲的', '苹果的', '花生的', '炸鸡的', '煎饼的']
            nicknamelistt = ['孙悟空', '猪八戒', '唐僧', '猫', '狗', '哈士奇', '张飞', '达芬奇', '蓝皮鼠', '大脸猫', '皮卡丘', '忍者神龟', '皮皮璐', '小王']
            nickname = nicknamelistf[random.randint(0, 3)] + nicknamelists[random.randint(0, 4)] + nicknamelistt[
                random.randint(0, 13)] + num
            customer_pwd = "123456"
            gender = 0
            birth = '2019-05-09'
            openid = '12'
            try:
                user = UserInfo.objects.create(customer_name=uphone, customer_pwd=customer_pwd, nickname=nickname, gender=gender, birth=birth, openid=openid)
                wallet = Wallet.objects.create(customer=user, money=0, is_active=True, tran_password='123456')
            except ObjectDoesNotExist as e:
                logger.error(e)
            # user = UserInfo.objects.filter(customer_name=uphone)
            code = 1003
            msg = "注册成功"
            # jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
            # jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
            # logininfo = jwt_payload_handler(user)
            # token = jwt_encode_handler(logininfo)
            data = {}
            data['uid'] = user.id
            data['avatar'] = str(user.avatar)
            data['sex'] = user.gender
            data['username'] = user.customer_name
            # data['token'] = token
        return JsonResponse({"code": code, "data": data, "msg": msg})


class CustomerInfo(APIView):

    def post(self, request):
        customer_id = request.POST.get("uid", '')
        retoken = request.POST.get("token", '')
        code = 1001
        data = {}
        customer = UserInfo.objects.filter(id=customer_id)
        if customer:
            code = 1000
            data['logo'] = str(customer[0].avatar)
            data['username'] = customer[0].nickname
            data['uid'] = customer[0].id
            data['moneybag'] = 'null'
            msg = '个人信息获取成功'
        else:
            code = 1001
            data['logo'] = ''
            data['username'] = ''
            data['uid'] = ''
            data['moneybag'] = 'null'
            msg = '个人信息获取失败'
        return JsonResponse({"code": code, "data": data, "msg": msg})



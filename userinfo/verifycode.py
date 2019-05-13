#!/usr/bin/python
# coding:utf-8

# django
# from django.http import JsonResponse

# base
import urllib.request, json
import random
# import os
# os.environ['DJANGO_SETTINGS_MODULE'] = 'uftc.settings'

class SendVerifyCode(object):

    def __init__(self, mobile):
        self.__mobile = mobile
        self.__randomcode = self.randomcode()
        self.__sendsms = self.sendsms()

    def randomcode(self):
        str = ""
        for i in range(6):
            ch = chr(random.randrange(ord('0'), ord('9') + 1))
            str += ch
        return str

    def sendsms(self):
        mobile = self.__mobile
        random_code = self.__randomcode
        appkey = '18954d5c773b50a7ebcc4f90d2bc3380'  # 您申请的短信服务appkey
        tpl_id = '157327'  # 申请的短信模板ID,根据实际情况修改
        tpl_value = '#code#={}'.format(random_code)  # 短信模板变量,根据实际情况修改

        sendurl = 'http://v.juhe.cn/sms/send'  # 短信发送的URL,无需修改

        params = 'key=%s&mobile=%s&tpl_id=%s&tpl_value=%s' % \
                 (appkey, mobile, tpl_id, urllib.request.quote(tpl_value))  # 组合参数

        wp = urllib.request.urlopen(sendurl + "?" + params)
        content = wp.read()  # 获取接口返回内容

        result = json.loads(content.decode())
        # print(result)
        # {'error_code': 0, 'result': {'sid': '5100945521111', 'fee': 1, 'count': 1}, 'reason': '操作成功'}

        if result:
            error_code = result['error_code']
            if error_code == 0:
                # 发送成功
                smsid = result['result']['sid']
                verifycode = random_code
                sendsms = "success"
                return json.dumps({"smsid": smsid, "verifycode": verifycode, "sendsms": sendsms})
                # return JsonResponse({"smsid": smsid, "verifycode": verifycode, "sendsms": sendsms})
                # print("sendsms success,smsid: %s" % (smsid))
                # sendsms success, smsid: 5100945521111
            else:
                # 发送失败
                sendsms = "error"
                error_code = error_code
                reason = result['reason']
                return json.dumps({"sendsms": sendsms, "error_code": error_code, "reason": reason})
                # return JsonResponse({"sendsms": sendsms, "error_code": error_code, "reason": reason})
                # print("sendsms error :(%s) %s" % (error_code, result['reason']))
        else:
            # 请求失败
            sendsms = "request sendsms error"
            return json.dumps({"sendsms": sendsms})
            # return JsonResponse({"sendsms": sendsms})
            # print("request sendsms error")


# if __name__ == '__main__':
#     result = SendVerifyCode("15133332563")
#     result_dict = json.loads(result._SendVerifyCode__sendsms)
#     print(result_dict)


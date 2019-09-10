# -*- coding: utf-8 -*-
import logging
import traceback
import random
import hashlib
import urllib
import xml.etree.ElementTree as ET

from django.conf import settings
from django.http import HttpResponse


from alipay.aop.api.AlipayClientConfig import AlipayClientConfig
from alipay.aop.api.DefaultAlipayClient import DefaultAlipayClient
from alipay.aop.api.FileItem import FileItem
from alipay.aop.api.domain.AlipayTradeAppPayModel import AlipayTradeAppPayModel
from alipay.aop.api.domain.AlipayTradeWapPayModel import AlipayTradeWapPayModel
from alipay.aop.api.domain.AlipayTradePagePayModel import AlipayTradePagePayModel
from alipay.aop.api.domain.AlipayTradePayModel import AlipayTradePayModel
from alipay.aop.api.domain.GoodsDetail import GoodsDetail
from alipay.aop.api.domain.SettleDetailInfo import SettleDetailInfo
from alipay.aop.api.domain.SettleInfo import SettleInfo
from alipay.aop.api.domain.SubMerchant import SubMerchant
from alipay.aop.api.request.AlipayOfflineMaterialImageUploadRequest import AlipayOfflineMaterialImageUploadRequest
from alipay.aop.api.request.AlipayTradeAppPayRequest import AlipayTradeAppPayRequest
from alipay.aop.api.request.AlipayTradePagePayRequest import AlipayTradePagePayRequest
from alipay.aop.api.request.AlipayTradePayRequest import AlipayTradePayRequest
from alipay.aop.api.request.AlipayTradeWapPayRequest import AlipayTradeWapPayRequest
from alipay.aop.api.response.AlipayOfflineMaterialImageUploadResponse import AlipayOfflineMaterialImageUploadResponse
from alipay.aop.api.response.AlipayTradePayResponse import AlipayTradePayResponse
from alipay.aop.api.util.SignatureUtils import verify_with_rsa

from urllib import parse


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s',
    filemode='a',)
logger = logging.getLogger('')


class AlipayAPI(object):

    def __init__(self):
        self._alipy_apps = settings.ALIPAY_APP
        self.alipay_client_config = AlipayClientConfig()
        self.alipay_client_config.server_url = 'https://openapi.alipay.com/gateway.do'
        self.alipay_client_config.app_id = '2018080360972019'
        self.alipay_client_config.sign_type = 'RSA2'
        self.alipay_client_config.charset = 'UTF-8'
        self.alipay_client_config.app_private_key = self._alipy_apps['ALIPAY_APP_PRIVATE_KEY']
        self.alipay_client_config.alipay_public_key = self._alipy_apps['ALIPAY_ALI_PUBLIC_KEY']

    def TradeWapPay(self, body, out_trade_no, total_amount):
        client = DefaultAlipayClient(alipay_client_config=self.alipay_client_config, logger=logger)
        model = AlipayTradeWapPayModel()
        model.body = body
        model.subject = 'parkingpay'
        model.out_trade_no = out_trade_no
        model.total_amount = total_amount
        model.product_code = 'QUICK_WAP_WAY'
        request = AlipayTradeWapPayRequest(biz_model=model)
        response = client.sdk_execute(request)
        print("alipayhm.trade.wap.pay response:" + str(response))
        return str(response)

    def TradeAppPay(self, body, subject, out_trade_no, total_amount):
        client = DefaultAlipayClient(alipay_client_config=self.alipay_client_config, logger=logger)
        model = AlipayTradeAppPayModel()
        model.body = body
        model.subject = subject
        model.out_trade_no = out_trade_no
        model.total_amount = '0.01'
        model.timeout_express = self._alipy_apps['ALIPAY_TIMEOUT_EXPRESS']
        model.product_code = 'QUICK_MSECURITY_PAY'
        request = AlipayTradeAppPayRequest(biz_model=model)
        request.notify_url = self._alipy_apps['ALIPAY_NOTIFY_URL']
        response = client.sdk_execute(request)
        return str(response)

    def CheckAppPay(self, params):
        sign = params.pop('sign', None)  # 取出签名
        params.pop('sign_type')  # 取出签名类型
        params = sorted(params.items(), key=lambda e: e[0], reverse=False)  # 取出字典元素按key的字母升序排序形成列表
        message = "&".join(u"{}={}".format(k, v) for k, v in params).encode()  # 将列表转为二进制参数字符串
        # with open(settings.ALIPAY_PUBLIC_KEY_PATH, 'rb') as public_key: # 打开公钥文件
        try:
            #     status =verify_with_rsa(public_key.read().decode(),message,sign) # 验证签名并获取结果
            status = verify_with_rsa(self.alipay_client_config.alipay_public_key.encode('utf-8').decode('utf-8'), message, sign)  # 验证签名并获取结果
            return status  # 返回验证结果
        except:  # 如果验证失败，返回假值。
            return False


class WXpayAPI(object):

    def __init__(self):
        self._wx_apps = settings.WX_APP
        self.appid = self._wx_apps['WX_APP_ID']
        self.mch_id = self._wx_apps['WX_MCH_ID']
        self.notify_url = self._wx_apps['WX_NOTIFY_URL']
        self.key = self._wx_apps['WX_SELF_KEY']

    def TradeAppPay(self, body, out_trade_no, total_fee, spbill_create_ip):
        appid = self.appid
        mch_id = self.mch_id
        nonce_str = self.createNoncestr()
        sign_type = 'MD5'
        device_info = 'WEB'
        body = body
        out_trade_no = out_trade_no
        fee_type = 'CNY'
        total_fee = int(total_fee)
        spbill_create_ip = spbill_create_ip
        notify_url = self.notify_url
        trade_type = 'APP'
        parameters = {}
        parameters["appid"] = str(appid)
        parameters["mch_id"] = mch_id
        parameters["nonce_str"] = nonce_str
        parameters["device_info"] = device_info
        parameters["sign_type"] = sign_type
        parameters["body"] = body
        parameters["out_trade_no"] = out_trade_no
        parameters["fee_type"] = fee_type
        parameters["total_fee"] = int(total_fee)
        parameters["spbill_create_ip"] = spbill_create_ip
        parameters["notify_url"] = notify_url
        # timeStamp = int(time.time())
        # parameters["timeStamp"] = "{0}".format(timeStamp)
        parameters["trade_type"] = trade_type
        sign = self.creatsign(parameters)
        parameters["sign"] = sign
        xml = self.arrayToXml(parameters)
        url = "https://api.mch.weixin.qq.com/pay/unifiedorder"
        request = urllib.Request(url)
        request.add_header('Content-Type', 'test/xml; charset="UTF-8"')
        responsea = urllib.urlopen(request, xml)
        sxs = responsea.read()
        data = self.to_dict(sxs)
        print(data['prepay_id'])



    def formatBizQueryParaMap(self, paraMap, urlencode):
        """格式化参数，签名过程需要使用"""
        slist = sorted(paraMap)
        buff = []
        for k in slist:
            v = parse.quote(paraMap[k]) if urlencode else paraMap[k]
            buff.append("{0}={1}".format(k, v))
        return "&".join(buff)

    def createNoncestr(self, length=32):
        """产生随机字符串，不长于32位"""
        chars = "abcdefghijklmnopqrstuvwxyz0123456789"
        strs = []
        for x in range(length):
            strs.append(chars[random.randrange(0, len(chars))])
        return "".join(strs)

    def creatsign(self, signs):
        stringB = self.formatBizQueryParaMap(signs, False)
        stringSignTemp = stringB + "&key="+self.key
        sign = hashlib.md5(self.to_utf8(stringSignTemp)).hexdigest().upper()
        return sign


    def arrayToXml(self, arr):
        """array转xml"""
        xml = ["<xml>"]
        for k, v in arr.iteritems():
            # if k=='attch'or k=='sign' or k=='body':
            # 	xml.append("<{0}><![CDATA[{1}]]></{0}>".format(k, v))
            # else:
            # xml.append("<{0}><![CDATA[{1}]]></{0}>".format(k, v))
            # xml.append("<{0}>{1}</{0}>".format(k, v))
            xml.append("<{0}>{1}</{0}>".format(k, v))
        xml.append("</xml>")
        return "".join(xml)


    def to_dict(self, xml):
        array_data = {}
        root = ET.fromstring(xml)
        for child in root:
            value = child.text
            array_data[child.tag] = value
        return array_data


if __name__ == '__main__':
    # body, out_trade_no, total_fee, spbill_create_ip
    WXpayAPI().TradeAppPay('a', '123456798456', 0.01,)


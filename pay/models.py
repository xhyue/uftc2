from django.db import models
from parking.models import *
from userinfo.models import *
from backend.models import *


# Create your models here.

PAY_STATUS = (
    (0, '成功'),
    (1, '失败'),
    (2, '支付中'),
    (3, '取消'),
)

WITHDRAW_STATUS = (
    (0, '成功'),
    (1, '失败'),
    (2, '提现中'),
    (3, '取消'),
)


class Bank(models.Model):
    bank_name = models.CharField(verbose_name='银行名称', max_length=50)
    is_delete = models.BooleanField(verbose_name='是否删除', default=False)

    def __str__(self):
        return self.bank_name

    class Meta:
        verbose_name = '银行表'
        verbose_name_plural = verbose_name


class Wallet(models.Model):
    customer = models.ForeignKey('userinfo.UserInfo', verbose_name='用户')
    money = models.DecimalField(verbose_name='金额', decimal_places=2, max_digits=8)
    is_active = models.BooleanField(verbose_name='是否激活', default=False)
    tran_password = models.CharField(verbose_name='交易密码', max_length=200)

    def __str__(self):
        return self.customer.customer_name

    class Meta:
        verbose_name = '钱包表'
        verbose_name_plural = verbose_name


class RechargeRecord(models.Model):
    customer = models.ForeignKey('userinfo.UserInfo', verbose_name='用户')
    charge_mode = models.ForeignKey(Bank, verbose_name='充值方式')
    charge_money = models.DecimalField(verbose_name='充值金额', decimal_places=2, max_digits=8)
    charge_date = models.DateTimeField(verbose_name='充值时间')
    pay_status = models.IntegerField(verbose_name='支付状态', choices=PAY_STATUS, default=0)

    def __str__(self):
        return self.customer.customer_name

    class Meta:
        verbose_name = '充值记录表'
        verbose_name_plural = verbose_name


class WithdrawRecord(models.Model):
    customer = models.ForeignKey('userinfo.UserInfo', verbose_name='用户')
    withdraw_mode = models.ForeignKey(Bank, verbose_name='提现方式')
    withdraw_money = models.DecimalField(verbose_name='提现金额', decimal_places=2, max_digits=8)
    withdraw_date = models.DateTimeField(verbose_name='提现时间')
    withdraw_status = models.IntegerField(verbose_name='提现状态', choices=PAY_STATUS, default=0)

    def __str__(self):
        return self.customer.customer_name

    class Meta:
        verbose_name = '提现记录表'
        verbose_name_plural = verbose_name


class PaymentRecord(models.Model):
    customer = models.ForeignKey('userinfo.UserInfo', verbose_name='用户')
    parking = models.ForeignKey('parking.ParkingLot', verbose_name='停车场')
    payment_money = models.DecimalField(verbose_name='支付金额', decimal_places=2, max_digits=8)
    payment_date = models.DateTimeField(verbose_name='支付时间')
    parking_record = models.ForeignKey('backend.ParkingRecord', verbose_name='停车记录')

    def __str__(self):
        return self.customer.customer_name

    class Meta:
        verbose_name = '支付记录表'
        verbose_name_plural = verbose_name

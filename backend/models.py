from django.db import models
from parking.models import *
from userinfo.models import *
from pay.models import *

# Create your models here.

class ParkingRecord(models.Model):
    customer = models.ForeignKey('userinfo.UserInfo', verbose_name='用户')
    parking = models.ForeignKey('parking.ParkingLot', verbose_name='停车场')
    parking_info = models.CharField(verbose_name='停车场信息', max_length=200)
    number_plate = models.CharField(verbose_name='车牌号', max_length=20)
    entry_time = models.DateTimeField(verbose_name='驶入时间')
    exit_time = models.DateTimeField(verbose_name='驶出时间')
    entry_picture = models.ImageField(verbose_name='驶入图片', upload_to='img/entry')
    exit_picture = models.ImageField(verbose_name='驶出图片', upload_to='img/exit')
    total_time = models.IntegerField(verbose_name='总时长')
    total_money = models.DecimalField(verbose_name='金额', decimal_places=2, max_digits=8)
    payment_mode = models.ForeignKey('pay.Bank', verbose_name='支付方式')

    def __str__(self):
        return self.customer.customer_name

    class Meta:
        verbose_name = '停车记录表'
        verbose_name_plural = verbose_name
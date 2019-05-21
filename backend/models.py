from django.db import models
from parking.models import *
from userinfo.models import *
from pay.models import *
import django.utils.timezone as timezone

# Create your models here.
CAR_TYPE = (
    ('0', '小型车'),
    ('1', '中型车'),
    ('2', '大型车'),
)


class ParkingRecord(models.Model):
    customer = models.ForeignKey('userinfo.UserInfo', verbose_name='用户')
    parking = models.ForeignKey('parking.ParkingLot', verbose_name='停车场')
    parking_info = models.CharField(verbose_name='停车场信息', max_length=200)
    number_plate = models.CharField(verbose_name='车牌号', max_length=20)
    entry_time = models.DateTimeField(verbose_name='驶入时间')
    exit_time = models.DateTimeField(verbose_name='驶出时间')
    entry_picture = models.ImageField(verbose_name='驶入图片', upload_to='img/entry/')
    exit_picture = models.ImageField(verbose_name='驶出图片', upload_to='img/exit/')
    total_time = models.IntegerField(verbose_name='总时长')
    total_money = models.DecimalField(verbose_name='金额', decimal_places=2, max_digits=8)
    payment_mode = models.ForeignKey('pay.Bank', verbose_name='支付方式')

    def __str__(self):
        return self.customer.customer_name

    class Meta:
        verbose_name = '停车记录表'
        verbose_name_plural = verbose_name


class ChargeStandard(models.Model):
    parking = models.ForeignKey('parking.ParkingLot', verbose_name='停车场')
    car_type = models.CharField(max_length=2, choices=CAR_TYPE, verbose_name='车型', default='0')
    day_money = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='白天价格')
    night_money = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='夜间价格')
    all_day_money = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='全天价格')
    time_unit = models.CharField(max_length=20, verbose_name='时间单位')
    start_time = models.TimeField(verbose_name='白天开始计费节点')
    end_time = models.TimeField(verbose_name='白天结束计费节点')
    add_date = models.DateTimeField(verbose_name='保存日期', default=timezone.now)
    mod_date = models.DateTimeField(verbose_name='最后修改日期', auto_now=True)
    average_price = models.DecimalField(verbose_name='平均价格', decimal_places=2, max_digits=6)

    def __str__(self):
        return self.car_type

    class Meta:
        db_table = 'standard'
        verbose_name = '收费标准'
        verbose_name_plural = verbose_name

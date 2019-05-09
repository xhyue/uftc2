from django.db import models
from userinfo.models import *
from parking.models import *


# Create your models here.


class TemporaryRecord(models.Model):
    customer = models.ForeignKey('userinfo.UserInfo', verbose_name='用户')
    parking = models.ForeignKey('parking.ParkingLot', verbose_name='停车场')
    number_plate = models.CharField(verbose_name='车牌号', max_length=20)
    plate_picture = models.ImageField(verbose_name='车牌图片', upload_to='img/temporary')
    entry_time = models.DateTimeField(verbose_name='驶入时间')

    def __str__(self):
        return self.customer.customer_name

    class Meta:
        verbose_name = '临时停车记录表'
        verbose_name_plural = verbose_name

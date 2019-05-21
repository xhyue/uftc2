from django.db import models
from userinfo.models import *
from pay.models import Bank

# Create your models here.

PARKING_LOT_TYPE = (
    (0, '室内'),
    (1, '室外'),
)

OWNER_TYPE = (
    (0, '自营'),
    (1, '加盟'),
    (2, '独立'),
)

CHECK_STATUS = (
    (0, '未审核'),
    (1, '审核成功'),
    (2, '审核失败'),
)

PARKING_TYPE = (
    (0, '出租'),
    (1, '临时'),
)

PARKING_STATUS = (
    (0, '维护中'),
    (1, '租赁中'),
    (2, '停车中'),
    (3, '空置中'),
)

PARKING_OWNER = (
    (0, '个人'),
    (1, '物业'),
)


DEVICE_STATUS = (
    (0, '未激活'),
    (1, '已激活'),
    (2, '故障中'),
    (3, '维修中'),
)


class ParkingLot(models.Model):
    property = models.ForeignKey('userinfo.Property', verbose_name='所属物业')
    parking_name = models.CharField(verbose_name='停车场名称', max_length=30)
    parking_type = models.IntegerField(verbose_name='停车场类型', choices=PARKING_LOT_TYPE, default=0)
    owner_type = models.IntegerField(verbose_name='所属权类型', choices=OWNER_TYPE, default=0)
    province = models.CharField(verbose_name='省', max_length=50)
    city = models.CharField(verbose_name='市', max_length=50)
    area = models.CharField(verbose_name='区', max_length=50)
    address = models.CharField(verbose_name='详细地址', max_length=200)
    longitude = models.DecimalField(verbose_name='经度', max_digits=60, decimal_places=20)
    latitude = models.DecimalField(verbose_name='维度', max_digits=60, decimal_places=20)
    total_number = models.IntegerField(verbose_name='总车位数')
    contact_info = models.CharField(verbose_name='联系方式', max_length=20)
    contact = models.CharField(verbose_name='联系人', max_length=20)
    remain_number = models.IntegerField(verbose_name='剩余车位数')
    banners = models.TextField(verbose_name='轮播图')
    device_number = models.IntegerField(verbose_name='设备数')
    is_active = models.BooleanField(verbose_name='是否激活', default=True)
    active_date = models.DateTimeField(verbose_name='激活日期')
    effect_time = models.IntegerField(verbose_name='有效时间')
    others = models.TextField(verbose_name='其他')

    def __str__(self):
        return self.parking_name

    class Meta:
        verbose_name = '停车场表'
        verbose_name_plural = verbose_name


class ParkingSpace(models.Model):
    customer = models.ForeignKey('userinfo.UserInfo', verbose_name='用户')
    parking = models.ForeignKey(ParkingLot, verbose_name='停车场')
    position = models.CharField(verbose_name='位置', max_length=200)
    parking_number = models.CharField(verbose_name='车位号', max_length=30)
    check_status = models.IntegerField(verbose_name='审核状态', choices=CHECK_STATUS, default=0)
    parking_type = models.IntegerField(verbose_name='车位类型', choices=PARKING_TYPE, default=1)
    parking_status = models.IntegerField(verbose_name='车位状态', choices=PARKING_STATUS, default=3)
    parking_picture = models.ImageField(verbose_name='车位图片', upload_to='img/parking')
    parking_owner = models.IntegerField(verbose_name='车位拥有者', choices=PARKING_OWNER, default=0)
    is_sensor = models.BooleanField(verbose_name='是否有车位传感器', default=False)
    sensor_number = models.CharField(verbose_name='车位传感器编号', max_length=30)

    def __str__(self):
        return self.parking_number

    class Meta:
        verbose_name = '车位表'
        verbose_name_plural = verbose_name


class Device(models.Model):
    parking = models.ForeignKey(ParkingLot, verbose_name='停车场')
    device_number = models.CharField(verbose_name='设备编号', max_length=30)
    device_type = models.IntegerField(verbose_name='设备类型')
    device_status = models.IntegerField(verbose_name='设备状态', choices=DEVICE_STATUS, default=0)

    def __str__(self):
        return self.device_number

    class Meta:
        verbose_name = '设备表'
        verbose_name_plural = verbose_name










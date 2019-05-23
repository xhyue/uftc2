from django.db import models
from django.contrib.auth.models import AbstractUser
from parking.models import ParkingLot

# Create your models here.
SEX_CHOICES = (
    (0, '男'),
    (1, '女'),
)


ADMIN_CHIOCES = (
    (0, "超级管理员"),
    (1, "物业"),
    (2, "停车场"),
    (3, "收费员"),
)

CAR_TYPE = (
    (1,"审核通过"),
    (2,"审核失败"),
    (3,"验证中"),
)




class UserInfo(models.Model):
    customer_name = models.CharField(verbose_name='用户', max_length=20, null=False, unique=True)
    customer_pwd = models.CharField(verbose_name='密码', max_length=200, null=False)
    nickname = models.CharField(verbose_name='昵称', max_length=20, null=False, unique=True)
    avatar = models.ImageField(verbose_name='头像', upload_to='img/avatar', default='')
    gender = models.IntegerField(verbose_name='性别', choices=SEX_CHOICES, default=0)
    birth = models.DateTimeField(verbose_name='生日')
    openid = models.CharField(verbose_name='微信id', max_length=200, null=True, blank=True)

    def __str__(self):
        return self.customer_name

    class Meta:
        verbose_name = '用户信息表'
        verbose_name_plural = verbose_name


class AdminInfo(AbstractUser):
    role = models.IntegerField(verbose_name="角色", choices=ADMIN_CHIOCES, default=0)
    parking = models.ForeignKey('parking.ParkingLot', verbose_name='所属停车场', null=True)
    expire_date = models.DateTimeField(verbose_name='过期时间', null=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = '管理员信息表'
        verbose_name_plural = verbose_name


class Property(models.Model):
    property_name = models.CharField(verbose_name='物业名称', max_length=30, null=False)
    property_ads = models.CharField(verbose_name='物业地址', max_length=200, null=False, unique=True)
    property_contact = models.CharField(verbose_name='联系方式', max_length=20)
    principal = models.OneToOneField(AdminInfo, verbose_name='负责人')

    def __str__(self):
        return self.property_name

    class Meta:
        verbose_name = '物业表'
        verbose_name_plural = verbose_name


class CarInfo(models.Model):
    customer = models.ForeignKey(UserInfo)
    brand = models.CharField(verbose_name='品牌', max_length=30, null=True)
    version = models.CharField(verbose_name='型号', max_length=30, null=True)
    type = models.IntegerField(verbose_name='审核进度',choices=CAR_TYPE,default=3)
    displacement = models.CharField(verbose_name='排量', max_length=30, null=True)
    plate = models.CharField(verbose_name='车牌号', max_length=30, null=True)
    drive_license = models.ImageField(verbose_name='车牌/驾驶证',upload_to='img/license/', null=True, default='normal.png')

    def __str__(self):
        return self.customer.customer_name

    class Meta:
        verbose_name = '车牌表'
        verbose_name_plural = verbose_name



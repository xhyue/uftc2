from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Bank)
admin.site.register(Wallet)
admin.site.register(RechargeRecord)
admin.site.register(WithdrawRecord)
admin.site.register(PaymentRecord)


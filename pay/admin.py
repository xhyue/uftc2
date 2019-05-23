from django.contrib import admin
from .models import *

# Register your models here.



class WalletAdmin(admin.ModelAdmin):
    list_display = ('customer','money','is_active')

    search_fields =('customer',) #搜索字段


admin.site.register(Bank)
admin.site.register(Wallet,WalletAdmin)
admin.site.register(RechargeRecord)
admin.site.register(WithdrawRecord)
admin.site.register(PaymentRecord)
from django.contrib import admin
from .models import *
#
#
# class WalletAdmin(admin.ModelAdmin):
#     list_display = ('customer', 'money', 'is_active')
#
#     search_fields =('customer',) #搜索字段
#
#     def has_add_permission(self, request):
#
#         if request.user != 'AnonymousUser':
#             if request.user.role == 0:
#                 return True
#             elif request.user.role == 1:
#                 return False
#             elif request.user.role == 2:
#                 return False
#             elif request.user.role == 3:
#                 return False
#             else:
#                 return False
#
#     def has_change_permission(self, request, obj=None):
#         if request.user != 'AnonymousUser':
#             if request.user.role == 0:
#                 return True
#             elif request.user.role == 1:
#                 return False
#             elif request.user.role == 2:
#                 return False
#             elif request.user.role == 3:
#                 return False
#             else:
#                 return False
#
#     def has_module_permission(self, request):
#
#         print(type(request.user))
#         if request.user != 'AnonymousUser':
#             if request.user.role == 0:
#                 return True
#             elif request.user.role == 1:
#                 return False
#             elif request.user.role == 2:
#                 return False
#             elif request.user.role == 3:
#                 return False
#             else:
#                 return False
#
#
# class BankAdmin(admin.ModelAdmin):
#     def has_add_permission(self, request):
#         if request.user != 'AnonymousUser':
#             if request.user.role == 0:
#                 return True
#             elif request.user.role == 1:
#                 return False
#             elif request.user.role == 2:
#                 return False
#             elif request.user.role == 3:
#                 return False
#             else:
#                 return False
#
#     def has_change_permission(self, request, obj=None):
#         if request.user != 'AnonymousUser':
#             if request.user.role == 0:
#                 return True
#             elif request.user.role == 1:
#                 return False
#             elif request.user.role == 2:
#                 return False
#             elif request.user.role == 3:
#                 return False
#             else:
#                 return False
#
#     def has_module_permission(self, request):
#
#         print(type(request.user))
#         if request.user != 'AnonymousUser':
#             if request.user.role == 0:
#                 return True
#             elif request.user.role == 1:
#                 return False
#             elif request.user.role == 2:
#                 return False
#             elif request.user.role == 3:
#                 return False
#             else:
#                 return False
#
#
# class RechargeRecordAdmin(admin.ModelAdmin):
#     def has_add_permission(self, request):
#         if request.user != 'AnonymousUser':
#             if request.user.role == 0:
#                 return True
#             elif request.user.role == 1:
#                 return False
#             elif request.user.role == 2:
#                 return False
#             elif request.user.role == 3:
#                 return False
#             else:
#                 return False
#
#     def has_change_permission(self, request, obj=None):
#         if request.user != 'AnonymousUser':
#             if request.user.role == 0:
#                 return True
#             elif request.user.role == 1:
#                 return False
#             elif request.user.role == 2:
#                 return False
#             elif request.user.role == 3:
#                 return False
#             else:
#                 return False
#
#     def has_module_permission(self, request):
#
#         print(type(request.user))
#         if request.user != 'AnonymousUser':
#             if request.user.role == 0:
#                 return True
#             elif request.user.role == 1:
#                 return False
#             elif request.user.role == 2:
#                 return False
#             elif request.user.role == 3:
#                 return False
#             else:
#                 return False
#
#
# class WithdrawRecordAdmin(admin.ModelAdmin):
#     def has_add_permission(self, request):
#         if request.user != 'AnonymousUser':
#             if request.user.role == 0:
#                 return True
#             elif request.user.role == 1:
#                 return False
#             elif request.user.role == 2:
#                 return False
#             elif request.user.role == 3:
#                 return False
#             else:
#                 return False
#
#     def has_change_permission(self, request, obj=None):
#         if request.user != 'AnonymousUser':
#             if request.user.role == 0:
#                 return True
#             elif request.user.role == 1:
#                 return False
#             elif request.user.role == 2:
#                 return False
#             elif request.user.role == 3:
#                 return False
#             else:
#                 return False
#
#     def has_module_permission(self, request):
#         if request.user != 'AnonymousUser':
#             if request.user.role == 0:
#                 return True
#             elif request.user.role == 1:
#                 return False
#             elif request.user.role == 2:
#                 return False
#             elif request.user.role == 3:
#                 return False
#             else:
#                 return False
#
#
# class PaymentRecordAdmin(admin.ModelAdmin):
#     def has_add_permission(self, request):
#         if request.user != 'AnonymousUser':
#             if request.user.role == 0:
#                 return True
#             elif request.user.role == 1:
#                 return False
#             elif request.user.role == 2:
#                 return False
#             elif request.user.role == 3:
#                 return False
#             else:
#                 return False
#
#     def has_change_permission(self, request, obj=None):
#         if request.user != 'AnonymousUser':
#             if request.user.role == 0:
#                 return True
#             elif request.user.role == 1:
#                 return False
#             elif request.user.role == 2:
#                 return True
#             elif request.user.role == 3:
#                 return False
#             else:
#                 return False
#
#     def has_module_permission(self, request):
#         print(type(request.user))
#         if request.user != 'AnonymousUser':
#             if request.user.role == 0:
#                 return True
#             elif request.user.role == 1:
#                 return False
#             elif request.user.role == 2:
#                 return True
#             elif request.user.role == 3:
#                 return False
#             else:
#                 return False
#
#
# admin.site.register(Bank, BankAdmin)
# admin.site.register(Wallet,WalletAdmin)
# admin.site.register(RechargeRecord, RechargeRecordAdmin)
# admin.site.register(WithdrawRecord, WithdrawRecordAdmin)
# admin.site.register(PaymentRecord, PaymentRecordAdmin)
#
admin.site.register(Bank)
admin.site.register(Wallet)
admin.site.register(RechargeRecord)
admin.site.register(WithdrawRecord)
admin.site.register(PaymentRecord)
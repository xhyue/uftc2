from django.contrib import admin
from .models import *

#
# class ParkingRecordAdmin(admin.ModelAdmin):
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
#                 return True
#             elif request.user.role == 2:
#                 return True
#             elif request.user.role == 3:
#                 return True
#             else:
#                 return False
#
#     def has_module_permission(self, request):
#         if request.user != 'AnonymousUser':
#             if request.user.role == 0:
#                 return True
#             elif request.user.role == 1:
#                 return True
#             elif request.user.role == 2:
#                 return True
#             elif request.user.role == 3:
#                 return False
#             else:
#                 return False
#
#
# class ChargeStandardAdmin(admin.ModelAdmin):
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
#                 return True
#             elif request.user.role == 2:
#                 return True
#             elif request.user.role == 3:
#                 return True
#             else:
#                 return False
#
#     def has_module_permission(self, request):
#         if request.user != 'AnonymousUser':
#             if request.user.role == 0:
#                 return True
#             elif request.user.role == 1:
#                 return True
#             elif request.user.role == 2:
#                 return True
#             elif request.user.role == 3:
#                 return False
#             else:
#                 return False


# Register your models here.
# admin.site.register(ParkingRecord, ParkingRecordAdmin)
# admin.site.register(ChargeStandard, ChargeStandardAdmin)
# Register your models here.
admin.site.register(ParkingRecord)
admin.site.register(ChargeStandard)
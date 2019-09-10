from django.contrib import admin
from .models import *

#
# class ParkingLotAdmin(admin.ModelAdmin):
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
#                 return True
#             elif request.user.role == 2:
#                 return False
#             elif request.user.role == 3:
#                 return False
#             else:
#                 return False
#
#
# class ParkingSpaceAdmin(admin.ModelAdmin):
#     def has_add_permission(self, request):
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
#     def has_change_permission(self, request, obj=None):
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
# class DeviceAdmin(admin.ModelAdmin):
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

# admin.site.register(ParkingLot, ParkingLotAdmin)
# admin.site.register(ParkingSpace, ParkingSpaceAdmin)
# admin.site.register(Device, DeviceAdmin)

admin.site.register(ParkingLot)
admin.site.register(ParkingSpace)
admin.site.register(Device)

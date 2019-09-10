from django.contrib import admin
from .models import *

# Register your models here.


# class CarInfoAdmin(admin.ModelAdmin):
#     def has_add_permission(self, request):
#         if request.user.role == 0:
#             return False
#         return True
#     def has_change__permission(self, request):
#         if request.user.role == 0:
#             return False
#         return True


admin.site.register(UserInfo)
admin.site.register(AdminInfo)
admin.site.register(Property)
admin.site.register(CarInfo)
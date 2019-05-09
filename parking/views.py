# restful API
from rest_framework.views import APIView

# django
from django.http import JsonResponse


from django.shortcuts import render

# Create your views here.


class IndexView(APIView):
    def post(self, request):
        longitude = request.POST.get("longitude", '')
        latitude = request.POST.get("latitude", '')
        print(longitude, latitude)
        # if longitude == "" or latitude == "":
        #     code = 1001
        #     shuju = []
        #     msg = "参数不能为空"
        #     return JsonResponse({"code": code, "shuju": shuju, "msg": msg})
        # if type(eval(longitude)) != float or type(eval(latitude)) != float:
        #     code = 1001
        #     shuju = []
        #     msg = "参数格式有误"
        #     return JsonResponse({"code": code, "shuju": shuju, "msg": msg})
        code = 1000
        shuju = [
            {
                "longitude": 116.32664152046861,
                "latitude": 39.96291960260539,
                "mg_id": 6,
                "total": 45,
                "area": "滨江区",
                "address": "聚工路19号",
                "lo": 116.32664152046861,
                "la": 39.96291960260539,
                "markerAddress": "滨江区聚工路19号",
                "marker": "",
                "occupy": 0,
                "leftpos": 45
            },
        ]
        msg = "第一页信息获取成功"
        return JsonResponse({"code": code, "shuju": shuju, "msg": msg})







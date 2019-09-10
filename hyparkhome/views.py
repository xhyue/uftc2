# restful API
from rest_framework.views import APIView
from rest_framework_jwt.settings import api_settings

# django
from django.contrib.auth.hashers import check_password
from django.http import JsonResponse

# self_project
from userinfo.models import AdminInfo

# Create your views here.


class PCAdminLogin(APIView):

    def post(self, request):
        user_name = request.POST.get("user_name", "")
        password = request.POST.get("password", "")
        if user_name == "" or password == "":
            result = False
            data = ""
            error = "用户名密码不能为空"
            return JsonResponse({"result": result, "data": data, "error": error})
        user = AdminInfo.objects.filter(username=user_name)
        if not user:
            result = False
            data = ""
            error = "未查询到用户"
            return JsonResponse({"result": result, "data": data, "error": error})
        is_pwd = check_password(password, user[0].password)
        if not is_pwd:
            result = False
            data = ""
            error = "用户名密码不正确"
            return JsonResponse({"result": result, "data": data, "error": error})
        if user:
            jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
            jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
            payload = jwt_payload_handler(user[0])
            token = jwt_encode_handler(payload)
            data = {}
            data['token'] = token
            result = True
            data = data
            error = ""
            return JsonResponse({"result": result, "data": data, "error": error})




class CarPositionView(APIView):

    def get(self, request):
        pass

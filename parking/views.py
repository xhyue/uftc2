# restful API
from rest_framework.views import APIView



# django
from django.http import JsonResponse

from .models import *
from .serializers import *
from backend.models import *
from .baidumap import *

import math
# Create your views here.

# index park list
class IndexView(APIView):
    def post(self, request):
        longitude = request.POST.get("longitude", '')
        latitude = request.POST.get("latitude", '')
        if longitude == "" or latitude == "":
            code = 1001
            shuju = []
            msg = "参数不能为空"
            return JsonResponse({"code": code, "shuju": shuju, "msg": msg})
        if type(eval(longitude)) != float or type(eval(latitude)) != float:
            code = 1001
            shuju = []
            msg = "参数格式有误"
            return JsonResponse({"code": code, "shuju": shuju, "msg": msg})
        cflongitude = float(longitude)-10
        ctlongitude = float(longitude)+10
        cflatitude = float(latitude)-10
        ctlatitude = float(latitude)+10
        parking = ParkingLot.objects.filter(is_active =True, longitude__range=(cflongitude, ctlongitude), latitude__range=(cflatitude, ctlatitude))
        park_data = ParkingSerializer(parking, many=True)
        parking_data = park_data.data
        code = 1000
        shuju = parking_data
        msg = "信息获取成功"
        return JsonResponse({"code": code, "shuju": shuju, "msg": msg})

# used park list
class UsedView(APIView):

    def post(self, request):
        uid = request.POST.get('uid','')
        token = request.POST.get('token','')
        last_park = ParkingRecord.objects.filter(customer_id=uid).order_by('-exit_time')
        if len(last_park) > 0:
            last_park = last_park[0]
        else:
            code = 1000
            data = []
            msg = "无最近使用"
            return JsonResponse({"code": code, "data": data, "msg": msg})
        code = 1000
        data = LastParkingSerializer(last_park, many=False).data
        msg = "信息获取成功"
        return JsonResponse({"code": code, "data": data, "msg": msg})


class GetRoute(APIView):

    def post(self, request):
        longitude = request.POST.get("longitude", '')
        latitude = request.POST.get("latitude", '')
        tlongitude = request.POST.get("longitude1", '')
        tlatitude = request.POST.get("latitude1", '')
        mg_id = request.POST.get("mg_id", '')
        data = {}
        print("mg_id",mg_id)
        parking = ParkingLot.objects.filter(id=mg_id)
        if len(parking) > 0:
            name = parking[0].parking_name
            result = GetDriving(longitude, latitude, tlongitude, tlatitude)
            distance = result.getDriving()
            data['name'] = name
            data['distance'] = distance
        else:
            code = 1001
            data = {}
            msg = "获取停车场失败"
            return JsonResponse({"code": code, "data": data, "msg": msg})
        charge = ChargeStandard.objects.filter(parking_id=mg_id)
        if len(charge) > 0:
            charge = charge[0].average_price
            data['charge'] = charge
        else:
            code = 1001
            data = {}
            msg = "获取金额失败"
            return JsonResponse({"code": code, "data": data, "msg": msg})
        data['mg_id'] = mg_id
        code = 1000
        data = data
        msg = "信息获取成功"
        return JsonResponse({"code": code, "data": data, "msg": msg})



class ParkingDetail(APIView):

    def post(self, request):
        longitude = request.POST.get("longitude", '')
        latitude = request.POST.get("latitude", '')
        mg_id = request.POST.get("mg_id", '')
        parking = ParkingLot.objects.filter(id=mg_id)
        if len(parking) == 0:
            code = 1001
            data = {}
            shuju = []
            msg = "信息获取失败"
            return JsonResponse({"code": code, "data": data, "shuju": shuju, "msg": msg})
        charge = ChargeStandard.objects.filter(parking_id=mg_id)
        if len(charge) == 0:
            code = 1001
            data = {}
            shuju = []
            msg = "信息获取失败"
            return JsonResponse({"code": code, "data": data, "shuju": shuju, "msg": msg})
        data = ParkingDetailSerializer(parking[0], many=False).data
        result = GetDriving(longitude, latitude, parking[0].longitude, parking[0].latitude)
        distance = result.getDriving()
        if distance == 0:
            code = 1001
            data = {}
            shuju = []
            msg = "信息获取失败"
            return JsonResponse({"code": code, "data": data, "shuju": shuju, "msg": msg})
        shuju = []
        shuju.append(str(parking[0].banners_one))
        shuju.append(str(parking[0].banners_two))
        shuju.append(str(parking[0].banners_three))
        data['distance'] = distance
        data['charge'] = charge[0].average_price
        code = 1000
        data = data
        shuju = shuju
        msg = "信息获取成功"
        return JsonResponse({"code": code, "data": data, "shuju": shuju, "msg": msg})


class SearchParking(APIView):

    def post(self, request):
        longitude = request.POST.get("longitude", '')
        latitude = request.POST.get("latitude", '')
        city = request.POST.get("city", '')
        city_list = {'秦皇岛市': '130300', '德州市': '371400', '镇江市': '321100', '淄博市': '370300', '西安市': '610100', '澄迈县': '469023', '黔东南苗族侗族自治州': '522600', '伊春市': '230700', '承德市': '130800', '朔州市': '140600', '苏州市': '320500', '平凉市': '620800', '广安市': '511600', '杭州市': '330100', '肇庆市': '441200', '临高县': '469024', '宁波市': '330200', '芜湖市': '340200', '晋城市': '140500', '南區': '810004', '楚雄彝族自治州': '532300', '辛集市': '139002', '鹰潭市': '360600', '滨州市': '371600', '南宁市': '450100', '怀化市': '431200', '南京市': '320100', '大庆市': '230600', '宿迁市': '321300', '黃大仙區': '810008', '舟山市': '330900', '菏泽市': '371700', '白城市': '220800', '常德市': '430700', '邯郸市': '130400', '盐城市': '320900', '萍乡市': '360300', '张家口市': '130700', '内江市': '511000', '大埔區': '810014', '定州市': '139001', '乐东黎族自治县': '469027', '定安县': '469021', '邢台市': '130500', '郴州市': '431000', '酒泉市': '620900', '珠海市': '440400', '仙桃市': '429004', '日照市': '371100', '桂林市': '450300', '海南藏族自治州': '632500', '本溪市': '210500', '克拉玛依市': '650200', '韶关市': '440200', '汉中市': '610700', '黄石市': '420200', '鹤壁市': '410600', '临沂市': '371300', '黔西南布依族苗族自治州': '522300', '六安市': '341500', '南通市': '320600', '枣庄市': '370400', '阿勒泰地区': '654300', '周口市': '411600', '海口市': '460100', '保亭黎族苗族自治县': '469029', '白沙黎族自治县': '469025', '莱芜市': '371200', '绵阳市': '510700', '阳江市': '441700', '荆州市': '421000', '佳木斯市': '230800', '上饶市': '361100', '宿州市': '341300', '哈尔滨市': '230100', '黄冈市': '421100', '沙田區': '810016', '阜阳市': '341200', '贺州市': '451100', '蚌埠市': '340300', '延安市': '610600', '石河子市': '659001', '大堂區': '820004', '邵阳市': '430500', '深水埗區': '810006', '朝阳市': '211300', '包头市': '150200', '巴音郭楞蒙古自治州': '652800', '绍兴市': '330600', '广州市': '440100', '河源市': '441600', '東區': '810003', '景德镇市': '360200', '哈密市': '650500', '乌兰察布市': '150900', '白银市': '620400', '平顶山市': '410400', '唐山市': '130200', '丽水市': '331100', '凉山彝族自治州': '513400', '济宁市': '370800', '牡丹江市': '231000', '淮南市': '340400', '怒江傈僳族自治州': '533300', '徐州市': '320300', '济源市': '419001', '台州市': '331000', '铁门关市': '659006', '青岛市': '370200', '梅州市': '441400', '九龍城區': '810007', '屯門區': '810011', '焦作市': '410800', '定西市': '621100', '遵义市': '520300', '赣州市': '360700', '汕头市': '440500', '和田地区': '653200', '泉州市': '350500', '新乡市': '410700', '商丘市': '411400', '咸宁市': '421200', '嘉峪关市': '620200', '阿克苏地区': '652900', '淮北市': '340600', '南平市': '350700', '临沧市': '530900', '铁岭市': '211200', '巴中市': '511900', '永州市': '431100', '锡林郭勒盟': '152500', '清远市': '441800', '合肥市': '340100', '拉萨市': '540100', '雅安市': '511800', '九江市': '360400', '抚顺市': '210400', '辽源市': '220400', '东莞市': '441900', '东方市': '469007', '鞍山市': '210300', '新余市': '360500', '保山市': '530500', '河池市': '451200', '海东市': '630200', '十堰市': '420300', '扬州市': '321000', '上海市': '310100', '贵港市': '450800', '广元市': '510800', '红河哈尼族彝族自治州': '532500', '郑州市': '410100', '延边朝鲜族自治州': '222400', '林芝市': '540400', '曲靖市': '530300', '开封市': '410200', '元朗區': '810012', '石家庄市': '130100', '玉林市': '450900', '张家界市': '430800', '儋州市': '460400', '长沙市': '430100', '昭通市': '530600', '临汾市': '141000', '辽阳市': '211000', '恩施土家族苗族自治州': '422800', '松原市': '220700', '塔城地区': '654200', '天水市': '620500', '亳州市': '341600', '文昌市': '469005', '安阳市': '410500', '洛阳市': '410300', '防城港市': '450600', '丹东市': '210600', '陵水黎族自治县': '469028', '甘孜藏族自治州': '513300', '聖方濟各堂區': '820008', '沧州市': '130900', '阿里地区': '542500', '金昌市': '620300', '德宏傣族景颇族自治州': '533100', '海西蒙古族藏族自治州': '632800', '西宁市': '630100', '日喀则市': '540200', '濮阳市': '410900', '万宁市': '469006', '烟台市': '370600', '路氹填海區': '820007', '南充市': '511300', '油尖旺區': '810005', '襄阳市': '420600', '花王堂區': '820002', '大兴安岭地区': '232700', '昌吉回族自治州': '652300', '银川市': '640100', '吐鲁番市': '650400', '榆林市': '610800', '五家渠市': '659004', '宜宾市': '511500', '廊坊市': '131000', '盘锦市': '211100', '文山壮族苗族自治州': '532600', '渭南市': '610500', '忻州市': '140900', '昆明市': '530100', '乌海市': '150300', '石嘴山市': '640200', '阿拉尔市': '659002', '潍坊市': '370700', '泸州市': '510500', '阜新市': '210900', '东营市': '370500', '三明市': '350400', '琼海市': '469002', '崇左市': '451400', '鄂尔多斯市': '150600', '四平市': '220300', '驻马店市': '411700', '重庆市': '500100', '阿拉善盟': '152900', '无锡市': '320200', '屯昌县': '469022', '庆阳市': '621000', '迪庆藏族自治州': '533400', '灣仔區': '810002', '孝感市': '420900', '漯河市': '411100', '通化市': '220500', '北區': '810013', '湘潭市': '430300', '眉山市': '511400', '中西區': '810001', '普洱市': '530800', '陇南市': '621200', '金华市': '330700', '厦门市': '350200', '安康市': '610900', '福州市': '350100', '三沙市': '460300', '大理白族自治州': '532900', '南阳市': '411300', '黄山市': '341000', '钦州市': '450700', '泰州市': '321200', '威海市': '371000', '贵阳市': '520100', '黔南布依族苗族自治州': '522700', '锦州市': '210700', '天津市': '120100', '吕梁市': '141100', '博尔塔拉蒙古自治州': '652700', '中山市': '442000', '长治市': '140400', '甘南藏族自治州': '623000', '兴安盟': '152200', '济南市': '370100', '果洛藏族自治州': '632600', '大同市': '140200', '保定市': '130600', '自贡市': '510300', '株洲市': '430200', '三门峡市': '411200', '云浮市': '445300', '龙岩市': '350800', '宜昌市': '420500', '信阳市': '411500', '湘西土家族苗族自治州': '433100', '吉安市': '360800', '衡水市': '131100', '呼伦贝尔市': '150700', '漳州市': '350600', '荆门市': '420800', '成都市': '510100', '毕节市': '520500', '觀塘區': '810009', '连云港市': '320700', '赤峰市': '150400', '马鞍山市': '340500', '乐山市': '511100', '滁州市': '341100', '衡阳市': '430400', '潜江市': '429005', '双鸭山市': '230500', '喀什地区': '653100', '武威市': '620600', '池州市': '341700', '南昌市': '360100', '梧州市': '450400', '来宾市': '451300', '绥化市': '231200', '随州市': '421300', '花地瑪堂區': '820001', '兰州市': '620100', '淮安市': '320800', '宜春市': '360900', '鄂州市': '420700', '柳州市': '450200', '琼中黎族苗族自治县': '469030', '宝鸡市': '610300', '阳泉市': '140300', '海北藏族自治州': '632200', '百色市': '451000', '宣城市': '341800', '北京市': '110100', '安顺市': '520400', '三亚市': '460200', '温州市': '330300', '昌江黎族自治县': '469026', '固原市': '640400', '莆田市': '350300', '武汉市': '420100', '汕尾市': '441500', '西双版纳傣族自治州': '532800', '沈阳市': '210100', '江门市': '440700', '湛江市': '440800', '图木舒克市': '659003', '風順堂區': '820005', '泰安市': '370900', '神农架林区': '429021', '茂名市': '440900', '望德堂區': '820003', '嘉兴市': '330400', '抚州市': '361000', '聊城市': '371500', '衢州市': '330800', '深圳市': '440300', '营口市': '210800', '铜仁市': '520600', '白山市': '220600', '铜陵市': '340700', '资阳市': '512000', '佛山市': '440600', '潮州市': '445100', '岳阳市': '430600', '吉林市': '220200', '齐齐哈尔市': '230200', '吴忠市': '640300', '丽江市': '530700', '七台河市': '230900', '離島區': '810018', '宁德市': '350900', '德阳市': '510600', '惠州市': '441300', '许昌市': '411000', '克孜勒苏柯尔克孜自治州': '653000', '西貢區': '810015', '常州市': '320400', '乌鲁木齐市': '650100', '六盘水市': '520200', '葵青區': '810017', '娄底市': '431300', '遂宁市': '510900', '玉溪市': '530400', '黄南藏族自治州': '632300', '长春市': '220100', '鹤岗市': '230400', '太原市': '140100', '达州市': '511700', '玉树藏族自治州': '632700', '台湾': '451200', '天门市': '429006', '呼和浩特市': '150100', '咸阳市': '610400', '中卫市': '640500', '鸡西市': '230300', '北海市': '450500', '黑河市': '231100', '嘉模堂區': '820006', '揭阳市': '445200', '临夏回族自治州': '622900', '张掖市': '620700', '通辽市': '150500', '益阳市': '430900', '葫芦岛市': '211400', '阿坝藏族羌族自治州': '513200', '运城市': '140800', '商洛市': '611000', '那曲地区': '542400', '铜川市': '610200', '昌都市': '540300', '大连市': '210200', '安庆市': '340800', '五指山市': '469001', '攀枝花市': '510400', '山南市': '540500', '晋中市': '140700', '荃灣區': '810010', '湖州市': '330500', '伊犁哈萨克自治州': '654000', '巴彦淖尔市': '150800'}
        city = city_list[city]
        content = request.POST.get("content", '')
        page = request.POST.get("page", 1)
        flag = request.POST.get("flag", 1)
        from_page = (int(page) - 1) * 10
        to_page = int(page) * 10 -1
        # parking = ParkingLot.objects.filter(city=city, id__range=(from_page, to_page))
        parking = ParkingLot.objects.filter(city=city)
        maxPage = ParkingLot.objects.filter(city=city).count()/10
        parking_list = []
        for pa in parking:
            park = {}
            park['mg_id'] = pa.id
            park['name'] = pa.parking_name
            park['occupy'] = 0
            park['charge'] = ChargeStandard.objects.filter(id=pa.id)[0].average_price
            park['address'] = pa.address
            park['leftpos'] = pa.remain_number
            park['destination_lo'] = pa.longitude
            park['destination_la'] = pa.latitude
            parking_list.append(park)
        # print("@@@@@@@@@",parking_list)
        result = GetNear(longitude, latitude, parking_list)
        data = result.getNear()
        if flag == '1':
            sorted_data = sorted(data, key=lambda data: data['diw'])[from_page:to_page]
        elif flag == '2':
            sorted_data = sorted(data, key=lambda data: data['charge'])[from_page:to_page]
        elif flag == '3':
            sorted_data = sorted(data, key=lambda data: data['leftpos'])[from_page:to_page]
        code = 1000
        data = sorted_data
        msg = "搜索停车场信息获取成功"
        maxpage = maxPage
        return JsonResponse({"code": code, "data": data, "maxpage":maxpage, "msg": msg})


# 获取个人录入车位信息
class GetSelfParking(APIView):

    def post(self, request):
        uid = request.POST.get("uid", '')
        page = request.POST.get("page", '')
        from_page = (int(page) - 1) * 10
        to_page = int(page) * 10 - 1
        parkingspace = ParkingSpace.objects.filter(customer_id=uid)
        maxPage = math.ceil(parkingspace.count()/10)
        padata = SelfParkingSerializer(parkingspace,many=True)
        data = {}
        pa_list = padata.data[from_page:to_page]
        code = 1000
        data['list'] = pa_list
        maxpage = maxPage
        msg = "车位信息获取成功"
        print(data,maxPage)
        return JsonResponse({"code": code, "data": data, "maxpage":maxpage, "msg": msg})





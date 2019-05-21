import json


def readjson(province,city,area,street):
    with open("./parking/json/areadata.json", 'r', encoding='utf-8') as json_file:
        t = json.load(json_file)
        data={}
        data["provice"] = t["86"][province]
        data["city"] = t[province][city]
        data["area"] = t[city][area]
        data["street"] = t[area][street]
        return data


def localjson(province,city,area,):

    with open("./parking/json/areadata.json", 'r', encoding='utf-8') as json_file:
        t = json.load(json_file)
        # print(province,city,area)
        data=t["86"][province] + t[province][city] + t[city][area]
        return data


def get_json_province(type):
    with open("./parking/json/areadata.json", 'r', encoding='utf-8') as json_file:
        t = json.load(json_file)
        provinces_data=t["86"]
        provinces = []
        citys = []
        areas = []
        for keyp, valuep in provinces_data.items():
            province = (keyp,valuep)
            provinces.append(province)
            if keyp != '710000':
                citys_data = t[keyp]
                for keyc, valuec in citys_data.items():
                    city = (keyc,valuec)
                    citys.append(city)
                    ni = ["469023","469005","469023","810015","441900","469006","469028","659001","659004","810013","460400","469027","429021","659002","429006","810004","820008","469001","659003","820001","139001","820002","659006","820005","820004","139002","820006","429005","820003","820007","469030","419001","810001","429004","620200","810018","810005","442000"]
                    if keyc in t.keys():
                        areas_data = t[keyc]
                        for keya, valuea in areas_data.items():
                            area = (keya, valuea)
                            areas.append(area)
        if type =="provinces":
            # print(tuple(provinces))
            return tuple(provinces)
        elif type == "citys":
            # print(tuple(citys))
            return tuple(citys)
        elif type == "areas":
            # print(tuple(areas))
            return tuple(areas)


if __name__ == '__main__':
	result = get_json_province("provinces")
	print(result)


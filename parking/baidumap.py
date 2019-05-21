from django.conf import settings
import requests
import json

from django.http import JsonResponse,request


class GetDriving(object):


    def __init__(self, origin_lo, origin_la, destination_lo, destination_la):
        self.__origin_lo = str('{:.6f}'.format(float(origin_lo)))
        self.__origin_la = str('{:.6f}'.format(float(origin_la)))
        self.__destination_lo = str('{:.6f}'.format(float(destination_lo)))
        self.__destination_la = str('{:.6f}'.format(float(destination_la)))
        self.__ak = 'GqohPozNne3cPFtPhkEu0KM4urYPZlTF'

    def getDriving(self):

        url = 'http://api.map.baidu.com/'
        api_url = 'direction/v2/driving'
        ak = self.__ak
        origin = self.__origin_la+','+self.__origin_lo
        destination = self.__destination_la+','+self.__destination_lo
        distance = 0
        params = {}
        params['origin'] = origin
        params['destination'] = destination
        params['ak'] = ak
        r = requests.get(url + api_url ,params=params)
        data = json.loads(r.text)
        distance = data['result']['routes'][0]['distance']
        print(distance)
        return distance



class GetNear(object):


    def __init__(self, origin_lo, origin_la, destination):
        self.__origin_lo = str('{:.6f}'.format(float(origin_lo)))
        self.__origin_la = str('{:.6f}'.format(float(origin_la)))
        self.__destination= destination

        self.__ak = 'GqohPozNne3cPFtPhkEu0KM4urYPZlTF'

    def getNear(self):

        url = 'http://api.map.baidu.com/'
        api_url = 'routematrix/v2/driving'
        ak = self.__ak
        origins = self.__origin_la+','+self.__origin_lo
        destination = ''
        totle = []
        for de in self.__destination:
            destination_lo = str('{:.6f}'.format(float(de['destination_lo'])))
            destination_la = str('{:.6f}'.format(float(de['destination_la'])))
            if destination:
                destination = destination +'|'+destination_la+','+destination_lo
            else:
                destination = destination_la+','+destination_lo
        destinations = destination
        if destinations:
            distance = 0
            params = {}
            params['origins'] = origins
            params['destinations'] = destinations
            params['ak'] = ak
            r = requests.get(url + api_url ,params=params)
            data = json.loads(r.text)
            # distance = data['result']['routes'][0]['distance']

            if data:
                distance = data['result']
                for inx,di in enumerate(distance):
                    if di['distance']['value'] >= 3000 and di['distance']['value'] < 4000:
                        self.__destination[inx]['distance'] = '>3.0km'
                    elif  di['distance']['value'] >= 4000 and di['distance']['value'] < 5000:
                        self.__destination[inx]['distance'] = '>4.0km'
                    elif  di['distance']['value'] >= 5000:
                        self.__destination[inx]['distance'] = '>5.0km'
                    else:
                        self.__destination[inx]['distance'] = str(di['distance']['value'])+"m"
                    self.__destination[inx]['diw'] = di['distance']['value']
            else:
                self.__destination[0]['distance'] = ''
            destination = self.__destination
            print(destination)
        return destination



if __name__ == '__main__':
    a = [{'mg_id':1,'destination_lo':116.452562,'destination_la':39.936404},{'mg_id':2,'destination_lo':116.852562,'destination_la':39.236404}]

    result = GetNear(116.339303,40.01116,a)
    n = result.getNear()

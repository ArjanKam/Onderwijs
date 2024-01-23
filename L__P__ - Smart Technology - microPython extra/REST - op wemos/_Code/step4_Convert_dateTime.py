import requests
import json
import datetime

def getIP():
    ip = requests.get('https://api.ipify.org').text
    return ip

def getLocation(ip):
    request = 'http://ip-api.com/json/' + ip
    result = requests.get(request)
    location = json.loads(result.text)
    return location["lat"], location["lon"], location["timezone"]

#http://worldtimeapi.org/api/timezone/Europe/Amsterdam
def getLocalTime(loction):
    request = 'http://worldtimeapi.org/api/timezone/' + loction
    result = requests.get(request)
    timezone = json.loads(result.text)
    return datetime.datetime.strptime(timezone["datetime"].split(".")[0]
                                           , '%Y-%m-%dT%H:%M:%S')
    
ip = getIP()
location = getLocation(ip)
date_time = getLocalTime(location[2])
print(type(date_time), date_time)



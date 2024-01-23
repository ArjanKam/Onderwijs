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

def string2Time(strValue):
    return datetime.datetime.strptime(strValue, '%I:%M:%S %p')
    
def riseSetSun(lat, long):
    request = r"https://api.sunrise-sunset.org/json?lat={}&lng={}&date=today".format(lat, long)
    result = requests.get(request)
    result = json.loads(result.text)["results"]
    return string2Time(result["sunrise"]), string2Time(result["sunset" ])

#returns True when now sun is down
def isNight(sunRise, sunSet, currentTime):
    if currentTime.time() < sunRise.time():
        return True
    if currentTime.time() > sunSet.time():
        return True
    return False

ip = getIP()
location = getLocation(ip)
date_time = getLocalTime(location[2])
sunRise, sunSet = riseSetSun(location[0], location[1])

print(sunRise, sunSet, date_time, isNight(sunRise, sunSet, date_time))



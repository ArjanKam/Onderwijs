import requests
import json

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
    return timezone["datetime"]
    
ip = getIP()
location = getLocation(ip)
print( getLocalTime(location[2]) )

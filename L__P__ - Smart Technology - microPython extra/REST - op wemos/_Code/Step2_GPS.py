import requests
import json

def getIP():
    ip = requests.get('https://api.ipify.org').text
    return ip

def getLocation(ip):
    request = 'http://ip-api.com/json/' + ip
    result = requests.get(request)
    server = json.loads(result.text)
    return server["lat"], server["lon"]

ip = getIP()
print( getLocation(ip) )

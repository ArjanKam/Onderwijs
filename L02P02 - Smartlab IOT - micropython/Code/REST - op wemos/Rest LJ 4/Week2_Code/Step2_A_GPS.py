import requests

def getIP():
    ip = requests.get('https://api.ipify.org').text
    return ip

def getLocation(ip):
    request = 'http://ip-api.com/json/' + ip
    result = requests.get(request).text
    return result

ip = getIP()
print( getLocation(ip) )

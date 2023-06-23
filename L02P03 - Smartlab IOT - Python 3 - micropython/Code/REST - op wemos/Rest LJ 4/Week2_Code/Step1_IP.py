import requests

def getIP():
    ip = requests.get('https://api.ipify.org').text
    return ip

print( getIP() )


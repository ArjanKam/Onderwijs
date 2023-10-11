import requests
import json
import datetime

def getIP():
    # This example requires the requests library be installed.
    # You can learn more about the Requests library
    # here: http://docs.python-requests.org/en/latest/
    ip = requests.get('https://api.ipify.org').text
    return ip

def getTime(ip):
    request = 'http://worldtimeapi.org/api/ip/' + ip
    result = requests.get(request)
    worldTime = json.loads(result.text)
    dateTime = worldTime["datetime"]
    #print(dateTime)
    date = datetime.datetime.strptime(dateTime[:10], '%Y-%m-%d')
    #print(date)
    time = datetime.datetime.strptime(dateTime[11:19], '%H:%M:%S').time()
    #print(time)
    dateTime = datetime.datetime.combine(date, time)
    return dateTime

def getLocation(ip):
    request = 'http://ip-api.com/json/' + ip
    result = requests.get(request)
    server = json.loads(result.text)
    return server["lat"], server["lon"]

#date in "%Y-%m-%d"
def riseSetSun(lat, long, dateTime):
    request = r"https://api.sunrise-sunset.org/json?"
    params = {"lat":lat, "lng":long, "date":dateTime.strftime("%Y-%m-%d")}
    result = requests.get(request, params=params)
    result = json.loads(result.text)["results"]
    sunrise = datetime.datetime.strptime(result["sunrise"], '%I:%M:%S %p').time()
    sunset  = datetime.datetime.strptime(result["sunset" ], '%I:%M:%S %p').time()
    return sunrise, sunset

def isDay(time, sunrise, sunset):
    return not isNight(time, sunrise, sunset)

def isNight(time, sunrise, sunset):
    #print(time, sunrise, sunset)
    if time < sunrise:
        return True
    if time > sunset:
        return True
    return False

if __name__ == "__main__":
    ip = getIP()
    print("ip=", ip)

    long, lat = getLocation(ip)
    print("long=",long, "lat=",lat)

    dateTime = getTime(ip)
    print("now=", dateTime )

    sunrise, sunset = riseSetSun(long, lat, dateTime)
    print("sunrise=",sunrise, "sunset=", sunset)

    if isNight(dateTime.time(), sunrise, sunset):
        print("Nacht")
    else:
        print("Dag")

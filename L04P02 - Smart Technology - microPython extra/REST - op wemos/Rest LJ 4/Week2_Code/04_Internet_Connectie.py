import machine
import sys
import network
import utime
import urequests
import json

WIFI_SSID     = "<YOUR WIFI SSID>"
WIFI_PASSWORD = "<YOUR WIFI PASSWORD>"
SLEEP = 5

# Get the external IP address from outside...
def getIP():
    return urequests.get('http://api.ipify.org/').text

def getLocation(ip):
    request = 'http://ip-api.com/json/' + ip
    result = urequests.get(request)
    server = json.loads(result.text)
    return server["lat"], server["lon"]

def time2Tuple(timeStr):
    parts = timeStr.split(":")
    last = parts[2].split(" ")
    hours = int(parts[0])
    if last[1] == "PM":
        hours = hours + 12
    return (hours, int(parts[1]), int(last[0]))

def riseSetSun(lat, long):
    request = r"https://api.sunrise-sunset.org/json?lat={}&lng={}&date=today".format(lat, long)
    result = urequests.get(request)
    result = json.loads(result.text)["results"]
    return time2Tuple(result["sunrise"]), time2Tuple(result["sunset" ])

def isDay(time, sunrise, sunset):
    return not isNight(time, sunrise, sunset)

def firstTupleSmallerInt(first, second, checkElements = 3):
    for pos in range(checkElements):
        if first[pos] < second[pos]:
            return True
        if first[pos] > second[pos]:
            return False
    return False

def firstTupleEqualInt(first, second, checkElements = 3):
    if first == None and second == None:
        return True
    if first == None or second == None:
        return False
    for pos in range(checkElements):
        if first[pos] < second[pos]:
            return False
        if first[pos] > second[pos]:
            return False
    return True

def isNight(time, sunrise, sunset):
    if firstTupleSmallerInt(time, sunrise):
        return True
    if firstTupleSmallerInt(sunset, time):
        return True
    return False

# Create a station object to store our connection
station = network.WLAN(network.STA_IF)
station.active(True)

long = None
lat = None
sunrise = None
sunset = None
lastDateChecked = None
def itsNight(externalIP):
    global sunrise
    global sunset
    global lastDateChecked
    dateTime = utime.localtime()
    currentDate = (dateTime[0],dateTime[1],dateTime[2])
    currentTime = (dateTime[3],dateTime[4],dateTime[5])
    
    if not firstTupleEqualInt(currentDate, lastDateChecked):
        lastDateChecked = currentDate
        sunrise, sunset = riseSetSun(long, lat)
        print("now=", currentTime, "sunrise=",sunrise, "sunset=", sunset)
    return isNight(currentTime, sunrise, sunset)
        
counter = 1
externalIp = None
# Continually try to connect to WiFi access point
while True:
    if not station.isconnected():
        # Try to connect to WiFi access point
        print(counter, "Connecting...")
        counter = counter + 1
        station.connect(WIFI_SSID, WIFI_PASSWORD)
        utime.sleep( SLEEP )
    if station.isconnected():
        # after is connected
        externalIp = getIP()
        print("Connected!")
        print("IP address : external {} internal{}".format(externalIp, station.ifconfig()[0]))
        long, lat = getLocation(externalIp)
        print("Location of device : long=",long, "lat=",lat)
    
    while station.isconnected():
        try:
            if itsNight(externalIp):
                print("Nacht")
            else:
                print("Dag")
            utime.sleep( SLEEP )
        except:
            print("An exception occurred")
            break
        

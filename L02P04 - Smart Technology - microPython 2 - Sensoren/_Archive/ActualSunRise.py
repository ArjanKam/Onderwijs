import machine
import sys
import network
import utime
import urequests
import json

__version__   = '0.1.0'
__author__    = 'Arjan Kamberg'
__copyright__ = "Arjan Kamberg"

SLEEP = 5
# Create a station object to store our connection
station = network.WLAN(network.STA_IF)
station.active(True)

class ActualSunRise:
    def __init__(self, ssid, password):
        self._ssid = ssid
        self._password = password
        self.counter = 1
        self.externalIp = None
        self.long = None
        self.lat = None
        self.sunrise = None
        self.sunset = None
        self.lastDateChecked = None
        self.connect()
        
    def info(self):
        night = self.getIsNight()
        return (self.lastDateChecked, night, self.long, self.lat, self.sunrise, self.sunset)
    
    def connected(self):
        while not station.isconnected():
            connect()
        return True
    
    def connect(self):
        if not station.isconnected():
            # Try to connect to WiFi access point
            print(self.counter, "Connecting...")
            self.counter = self.counter + 1
            station.connect(self._ssid, self._password)
            utime.sleep( SLEEP )
        if station.isconnected():
            # after is connected
            self.externalIp = self.getIP()
            print("Connected!")
            print("IP address : external {} internal{}".format(self.externalIp, station.ifconfig()[0]))
            self.long, self.lat = self.getLocation(self.externalIp)
            print("Location of device : long=",self.long, "lat=",self.lat)
        
    # Get the external IP address from outside...
    def getIP(self):
        return urequests.get('http://api.ipify.org/').text
    
    def getTime(self, ip):
        request = 'http://worldtimeapi.org/api/ip/' + ip
        result = urequests.get(request)
        worldTime = json.loads(result.text)
        dateTime = worldTime["datetime"]
        print(dateTime)
        datePart = dateTime[:10].split("-")
        timePart = dateTime[11:19].split(":")
        return (int(datePart[0]), int(datePart[1]), int(datePart[2]), 0, int(timePart[0]), int(timePart[1]), int(timePart[2]), 0)

    def getLocation(self, ip):
        request = 'http://ip-api.com/json/' + ip
        result = urequests.get(request)
        server = json.loads(result.text)
        return server["lat"], server["lon"]

    def time2Tuple(self, timeStr):
        parts = timeStr.split(":")
        last = parts[2].split(" ")
        hours = int(parts[0])
        if last[1] == "PM":
            hours = hours + 12
        return (hours, int(parts[1]), int(last[0]))

    def getRiseSetSun(self, lat, long):
        request = r"https://api.sunrise-sunset.org/json?lat={}&lng={}&date=today".format(lat, long)
        result = urequests.get(request)
        result = json.loads(result.text)["results"]
        return self.time2Tuple(result["sunrise"]), self.time2Tuple(result["sunset" ])

    def isDay(self, time, sunrise, sunset):
        return not self.isNight(time, sunrise, sunset)

    def firstTupleSmallerInt(self, first, second, checkElements = 3):
        for pos in range(checkElements):
            if first[pos] < second[pos]:
                return True
            if first[pos] > second[pos]:
                return False
        return False

    def firstTupleEqualInt(self, first, second, checkElements = 3):
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

    def isNight(self, time, sunrise, sunset):
        if self.firstTupleSmallerInt(time, sunrise):
            return True
        if self.firstTupleSmallerInt(sunset, time):
            return True
        return False

    def getIsNight(self):
        dateTime = utime.localtime()
        currentDate = (dateTime[0],dateTime[1],dateTime[2])
        currentTime = (dateTime[3],dateTime[4],dateTime[5])
        try:
            if not self.firstTupleEqualInt(currentDate, self.lastDateChecked):
                #Eveny day the RTC is updated with the internet-clock
                dateTime = self.getTime(self.externalIp)
                machine.RTC().datetime(dateTime)

                self.lastDateChecked = currentDate
                self.sunrise, self.sunset = self.getRiseSetSun(self.long, self.lat)
                print("now=", currentTime, "sunrise=",self.sunrise, "sunset=", self.sunset)
            return self.isNight(currentTime, self.sunrise, self.sunset)
        except:
            print("An error occured")
            return True
        

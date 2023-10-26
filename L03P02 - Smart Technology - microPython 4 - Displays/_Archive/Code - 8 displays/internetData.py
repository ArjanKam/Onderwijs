import network, urequests, utime, ntptime
from machine import Timer
import secrets
URL = "http://weerlive.nl/api/json-data-10min.php?key="+secrets.WEERLIVE_KEY+"&locatie=Dordrecht"
API_TIMER_DELAY      =  5 * 60 * 1000 # API query delay (ms)
CLOCK_TIMER_DELAY    = 15 * 60 * 1000 # clock update delay (ms)
MAX7219_INVERT       = False  # Invert MAX7219 display

# format string for displaying data
FORMAT = "{temp}C " \
      "{windr} {winds} " \
      "{luchtd} mbar " \
      "zon {sup}/{sunder} : " \
      "{verw}."

def getResponseData(response):
    data = response.json()['liveweer'][0]
    # generate formatted string
    output = FORMAT.format(**data)
    print(output)
    return output

data           = ""
data_available = False
timer_api      = Timer(-1)
timer_clock    = Timer(-1)

wifi = network.WLAN(network.STA_IF)
wifi.active(False)
def connect():
    global wifi
    # connect to WiFi
    print("Connecting to WiFi...")
    wifi.active(True)
    wifi.connect(secrets.SSID, secrets.PASSWORD)
    while not wifi.isconnected():
        print(".",end="")
        utime.sleep(0.4)
        pass
    print("Connected.")

# decorator for checking WiFi status
def wifi_check_decorator(func):
    def wrapper(*args, **kwargs):
        if not wifi.isconnected():
            # stop timers
            timer_api.deinit()
            timer_clock.deinit()
            timer_display.deinit()
            # reboot
            reset()
        else:
            # run decorated functions
            func(*args, **kwargs)
    return wrapper

# query time from NTP server
@wifi_check_decorator
def query_time(timer):
    print("Update Time")
    while True:
        try:
            ntptime.settime()
            break
        except:
            utime.sleep(1)

# query data from API
@wifi_check_decorator
def query_api(timer):
    global data, data_available
    try:
        data_available = False
        # query API
        response = urequests.get(URL)
        print(response.status_code)
        # query successful
        if response.status_code == 200:
            # parse data as dictionary
            data = getResponseData(response)
            response.close()
            data_available = True
    except:
        pass
    finally:
        pass

connect()

timer_clock.init(period=CLOCK_TIMER_DELAY,
                 mode=Timer.PERIODIC,
                 callback=query_time)

timer_api.init(period=API_TIMER_DELAY,
               mode=Timer.PERIODIC,
               callback=query_api)

# query time and data
print("Querying data for first time...")
query_time(None)
query_api(None)

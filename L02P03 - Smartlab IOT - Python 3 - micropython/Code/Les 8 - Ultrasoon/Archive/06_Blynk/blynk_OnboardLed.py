import BlynkLib
import network
import machine

WIFI_SSID     = "ESA_2_4GHz" #"<YOUR WIFI SSID>"
WIFI_PASS     = "S1m30nElsA6213" #"<YOUR WIFI PASSWORD>"
BLYNK_AUTH    = 'IFD3NI0oBH3agF_cu3bPL85Axj0e8XeY'
ONBOARD_LED   = 2 # Led on WeMos

led = machine.Pin( ONBOARD_LED, machine.Pin.OUT )

print("Connecting to WiFi...")
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(WIFI_SSID, WIFI_PASS)
while not wifi.isconnected():
    pass

print('IP:', wifi.ifconfig()[0])

print("Connecting to Blynk...")
blynk = BlynkLib.Blynk(BLYNK_AUTH) # , log=print

# Register Virtual Pins
@blynk.VIRTUAL_WRITE(0)
def my_write_handler(value):
    print('Current V1 value: {}'.format(value))
    if value[0] == '0':
        print("Off")
        led.off()
    else:
        print("On")
        led.on()

@blynk.VIRTUAL_READ(1)
def my_read_handler():
    # this widget will show some time in seconds..
    blynk.virtual_write(2, int(time.time()))

@blynk.on("connected")
def blynk_connected(ping):
    print('Blynk ready. Ping:', ping, 'ms')

def runLoop():
    while True:
        blynk.run()
        machine.idle()

# Run blynk in the main thread:
runLoop()
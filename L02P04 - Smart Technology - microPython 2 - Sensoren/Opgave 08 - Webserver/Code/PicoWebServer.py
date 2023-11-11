from machine import Pin
import network
import socket
import time
from secrets import *
from html_page import HTML

relay = Pin(16, Pin.OUT, Pin.PULL_UP)
led   = Pin("LED", Pin.OUT)

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(SSID, PASSWORD)

relayState = "Unknown"
def relay(id, on):
    global relayState
    if on:
        relay.value(1)
        relayState = "Relay is On"
    else:
        relay.value(0)
        relayState = "Relay is OFF"
    print(relayState)
relay(0,False)

def handleRequest(request):
    request = str(request)
    relay_on  = request.find('/relay/on')
    relay_off = request.find('/relay/off')
    print( 'relay on  = ' + str(relay_on))
    print( 'relay off = ' + str(relay_off))

    if relay_on == 6:
        relay(0, True)           

    if relay_off == 6:
        relay(0, False)     

# Wait for connect or fail
countdown = 10
while countdown > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    countdown -= 1
    print('.', end = "")
    time.sleep(1)

# Handle connection error
if wlan.status() != 3:
    raise RuntimeError('network connection failed')
else:
    print('connected')
    status = wlan.ifconfig()
    print( 'ip = ' + status[0] )
    for i in range (6):
        led.toggle()
        time.sleep_ms(200)

addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
s = socket.socket()
s.bind(addr)
s.listen(1)
print('listening on', addr)

while True:
    try:
        cl, addr = s.accept()
        print('client connected from', addr)
        request = cl.recv(1024)
        print(request)

        handleRequest(request) 
            
        response = HTML % relayState
        cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
        cl.send(response)
        cl.close()

    except OSError as e:
        cl.close()
        print('connection closed')
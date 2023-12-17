from machine import Pin
import network
import socket
import time
from secrets import *
from html_page import HTML

RELAY_PINS = (16,17,18,19,20,21,22,26)
relay_Pin = []
for pin in RELAY_PINS:
    relay_Pin.append(Pin(pin, Pin.OUT, Pin.PULL_UP))
relayOn = set()
for r in relay_Pin:
    r.off()
    
led = Pin("LED", Pin.OUT)

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(SSID, PASSWORD)

relayState = "Unknown"

def handleRelay(index, request):
    relay_on  = request.find(f'/relay/on{index}')
    relay_off = request.find('/relay/off'+str(index))
    print( f'relay on{index}  = ' + str(relay_on))
    print( f'relay off{index} = ' + str(relay_off))

    if relay_on == 6:
        relay_Pin[index-1].on()
        relayOn.add(index)
    if relay_off == 6:
        relay_Pin[index-1].off()
        relayOn.remove(index)
        
def handleRequest(request):
    global relayState
    request = str(request)
    relayState = "Relais on : "
    handleRelay(1, request)
    handleRelay(2, request)
    handleRelay(3, request)
    handleRelay(4, request)
    handleRelay(5, request)
    handleRelay(6, request)
    handleRelay(7, request)
    handleRelay(8, request)
    for on in relayOn:
        relayState += str(on) + " " 
        
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
    raise RuntimeError('network connection failed test')
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
        print(f' >> ERROR: {e}')

    finally:
        cl.close()
        #s.close()
        print('connection closed')
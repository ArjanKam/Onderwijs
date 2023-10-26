import secrets # store your SSIS and PASSWORD here
import network
import utime
MAX_DOTS = 4

#infoOutput = function(text)
def connect(disconnect = False, infoOutput = None):
    sta_if = network.WLAN(network.STA_IF)
    if disconnect == True:
        sta_if.disconnect()
    if not sta_if.isconnected():
        sta_if.active(True)
        sta_if.connect(secrets.SSID, secrets.PASSWORD)
        tries = 0
        while not sta_if.isconnected():
            if infoOutput != None:
                infoOutput("." * (tries % (MAX_DOTS + 1)))
                tries = tries + 1
            utime.sleep(1)
            pass


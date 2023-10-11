from umqttsimple import MQTTClient
import network
import utime
import wemos_constants as constants
from machine import ADC, Pin
import machine
import ubinascii


# Valve components Pin5 = D1
p2 = Pin(5, Pin.OUT)

# Moisture components
soil = ADC(0)
min_moisture = 0
max_moisture = 65535
readDelay = 0.5

# The connection to the network
station = network.WLAN(network.STA_IF)
station.active(True)

# Na elke publish de topic en de msg oppakken
def callback_data(topic, msg):
    print(topic, msg)

def connect():
    client = MQTTClient(ubinascii.hexlify(machine.unique_id()), "192.168.1.99", keepalive=60)
    client.set_callback(callback_data)
    client.connect()
    return client

# Returns the values of the HW-390 Moisture Sensor
def get_moisture():
    return ((max_moisture - soil.read_u16())*100/(max_moisture - min_moisture))


# Returns the value of the valve
def get_valve():
    return p2


# The main system that runs in a loop
counter = 1
while True:
    # Connect to the network
    if not station.isconnected():
        print(counter, "connecting...")
        counter = counter + 1
        station.connect(constants.network.host, constants.network.password)
        utime.sleep(5)

    # Check if system is connected to the network
    if (station.isconnected()):
            
        while True:

            # Send success message
            print("Connected !")
            print(station.ifconfig())

            # Try to connect to the MQTT system.
            try:
                print("Start try catch")
                client = connect()
                
                # Static getters
                moisture = get_moisture()
                
                print("moisture = " + str(moisture))
                
                # Send all data to MQTT server
                client.publish('G7/MOISTURE', str(moisture))

                # Get valve that return a 0 or a 1
                valve = client.subscribe("G7/VALVE")
                valve_waarde = p2
                print("valve = " + str(valve))
                
                if(moisture < 50):
                    p2(0)
                elif(moisture > 51):
                    p2(1)

                # Check print for console to see moisture and valve value's
                print("Published Moisture: " + str(moisture) + " Valve: " + str(valve))

                # Wait a little before continuing
                utime.sleep(5)

            # Send an exception
            except OSError as e:
                print(e)

            # Wait a little before continuing
            utime.sleep(5)

# A disabled print for checking the moisture system
# print("moisture: " + "%.2f" % get_moisture() + "% (adc: " + str(soil.read_u16()) + ")")

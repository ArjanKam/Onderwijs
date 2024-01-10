from machine import Pin, I2C
from time import sleep
#I2C Initialization
tc74address = 0x48
i2c_interface = 0
sdapin = Pin(16)
sclpin = Pin(17)

i2c =I2C(i2c_interface, scl=sclpin, sda=sdapin, freq=100000)

# Open File
file = open("tempdata.txt", "w")

# Write Data to File Function
def writefiledata(time, value):
    file.write(f"{time;{round(value, 2)}\n")

counter=0
SLEEP = 5 # sleep 5 seconds

while True:
    data = i2c.readfrom(tc74address, 1, True) temp = int.from_bytes(data, "big") print(temp)
    writefiledata(k*SLEEP, temp)
    counter += 1
    sleep(SLEEP)

file.close()


import serial
from time import sleep
# Configure the serial connection
port = "COM38" #"/dev/cu.URT1" 
baudrate = 115200
serial_connection = serial.Serial(port, baudrate)

# Read and write data until the transfer is complete
counter = 0
while True:
    if counter % 100 == 0:
        #inform the pico to move servo to 45 degrees
        serial_connection.write(b"45")
    else:
        sleep(0.2)
    counter += 1
    #wait for response of servo with angle and measurement.
    
    data = serial_connection.read(128)
    if data == b"EOF":
        break
    print(data)
        

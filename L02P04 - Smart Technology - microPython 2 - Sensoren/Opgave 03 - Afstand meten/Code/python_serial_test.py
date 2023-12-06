import serial

# Configure the serial connection
port = "COM3" #"/dev/cu.URT1" 
baudrate = 115200
serial_connection = serial.Serial(port, baudrate)

# Read and write data until the transfer is complete
def readDistance(angle):
    #serial_connection.write(b"{angle}")
    data = ""
    while True:
        char = serial_connection.read()
        if char == b"\n":
            data = ""
        elif char == b"\r":
            return(data)
        else:
           data += char.decode("utf-8")

while True:
    for angle in range(0,180,1):
        data = readDistance(angle).split(";")
        print(data)
        
        
        
import serial

# Configure the serial connection
<<<<<<< Updated upstream
port = "COM3" #"/dev/cu.URT1" 
=======
port = "COM38" #"/dev/cu.URT1" 
>>>>>>> Stashed changes
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
<<<<<<< Updated upstream
    for angle in range(0,180,1):
        data = readDistance(angle).split(";")
        print(data)
=======
    data = serial_connection.read(128)
    if data == b"EOF":
        break
    print(data)


>>>>>>> Stashed changes

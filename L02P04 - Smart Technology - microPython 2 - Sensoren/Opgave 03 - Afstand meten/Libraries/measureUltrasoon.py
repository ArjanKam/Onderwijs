import serial

# Configure the serial connection
port = "COM3" #"/dev/cu.URT1" 
baudrate = 115200
serial_connection = serial.Serial(port, baudrate)

# Read and write data until the transfer is complete
def readDistance():
    #encoded=str(angle).encode('utf-8')
    #serial_connection.write(encoded)
    data = ""
    while True:
        char = serial_connection.read()
        if char == b"\n":
            data = ""
        elif char == b"\r":
            data = data.split(";")
            return(int(data[0]), int(data[1]), float(data[2]))
        else:
           data += char.decode("utf-8")
           
if __name__ == "__main__":
    while True:
        for angle in range(0,180,1):
            data = readDistance(angle)
            print(data[0],data[1])

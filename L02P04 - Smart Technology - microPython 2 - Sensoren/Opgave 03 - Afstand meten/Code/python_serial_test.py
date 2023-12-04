import serial

# Configure the serial connection
port = "/dev/cu.URT1" 
baudrate = 115200
serial_connection = serial.Serial(port, baudrate)

# Read and write data until the transfer is complete
while True:
    data = serial_connection.read(128)
    if data == b"EOF":
        break
    print(data)
    
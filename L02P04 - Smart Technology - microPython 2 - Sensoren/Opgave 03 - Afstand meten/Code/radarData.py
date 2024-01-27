import serial

SERIAL_PORT = 'COM17'
BOUT_RATE   = 115200

# import measureUltrasoon as ultrasoon
ser = serial.Serial(SERIAL_PORT, BOUT_RATE)				# Create a serial object

def readData():
    data = ser.readline().decode('utf-8').strip() 	# Read a line from the serial port
    angle, distance = data.split(" ")
    angle = int(angle)
    distance = float(distance)
    distance *= 20
    if distance < 0:
        distance = 999
    return angle, distance

# Close the serial port when the program is interrupted (Ctrl+C)
#ser.close()
#print("Serial port closed.")

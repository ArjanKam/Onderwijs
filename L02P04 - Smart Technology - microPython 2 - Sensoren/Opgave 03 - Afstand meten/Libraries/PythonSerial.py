import serial

# Define the serial port and baud rate
serial_port = '/dev/ttyUSB0'  # Update this with your actual serial port
baud_rate   = 115200

ser = serial.Serial(serial_port, baud_rate)				# Create a serial object
try:
    while True:
        line = ser.readline().decode('utf-8').strip() 	# Read a line from the serial port
        print(line)										# Print the received data
except KeyboardInterrupt:
    # Close the serial port when the program is interrupted (Ctrl+C)
    ser.close()
    print("Serial port closed.")
    

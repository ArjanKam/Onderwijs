import machine
import utime

# Function to be executed by the timer
def periodic_action(timer):
    print("Performing periodic action...") # Add the action you want to perform here

# Create a timer object (Timer 0)
timer = machine.Timer(0)
# Configure the timer to call the periodic_action function every 5 seconds
timer.init(period=5000, mode=machine.Timer.PERIODIC, callback=periodic_action)

# Keep the main program running indefinitely
try:
    while True:
        utime.sleep(10)  # Sleep to reduce CPU usage
except KeyboardInterrupt:
    print("Program interrupted by user.")



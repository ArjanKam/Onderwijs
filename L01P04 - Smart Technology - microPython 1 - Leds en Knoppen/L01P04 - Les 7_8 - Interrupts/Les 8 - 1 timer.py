import threading
import time
TIME_INTERVAL_1 = 1.0
    
def periodic_action_1():
    print(".", end="")
    timer = threading.Timer(TIME_INTERVAL_1, periodic_action_1)  # Schedule next execution
    timer.start()
    
periodic_action_1() # Start the periodic action

try: # Keep the main thread alive so the periodic action can run
    while True:
        time.sleep(20)  # Keep the main thread alive
        print("20 seconden later")
except KeyboardInterrupt: #CTRL-C
    print("Program interrupted by user.")


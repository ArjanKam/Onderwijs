import threading
import time
TIME_INTERVAL_1 = 5.0
TIME_INTERVAL_2 = 20.0
    
def periodic_action_1():
    print(".", end="")
    timer = threading.Timer(TIME_INTERVAL_1, periodic_action_1)  # Schedule next execution
    timer.start()

def periodic_action_2():
    print("#", end="")
    timer = threading.Timer(TIME_INTERVAL_2, periodic_action_2)  # Schedule next execution
    timer.start()
    
periodic_action_1() # Start the periodic action
periodic_action_2() # Start the periodic action


try: # Keep the main thread alive so the periodic action can run
    while True:
        time.sleep(100)  # Keep the main thread alive
except KeyboardInterrupt: #CTRL-C
    print("Program interrupted by user.")


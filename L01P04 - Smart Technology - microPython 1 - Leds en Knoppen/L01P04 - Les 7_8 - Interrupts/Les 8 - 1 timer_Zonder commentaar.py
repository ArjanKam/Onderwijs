import threading
import time
TIME_INTERVAL_1 = 1.0
TIME_INTERVAL_2 = 20.0
    
def periodic_action_1():
    print(".", end="")
    timer = threading.Timer(TIME_INTERVAL_1, periodic_action_1)
    timer.start()

def periodic_action_2():
    print("#", end="")
    timer = threading.Timer(TIME_INTERVAL_2, periodic_action_2)
    timer.start()

periodic_action_1()
periodic_action_2()

# try:
#     while True:
#         time.sleep(2000)
#         #print("20 seconden later")
# except KeyboardInterrupt:
#     print("Program interrupted by user.")
# 

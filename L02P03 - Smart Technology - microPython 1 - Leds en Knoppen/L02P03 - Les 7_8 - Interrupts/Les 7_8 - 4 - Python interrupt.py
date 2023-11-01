import signal
from time import sleep

def signal_handler(sig, frame):
    print('@', end="")
    
# Interrupt from keyboard SIGINT => (CTRL + C).
signal.signal(signal.SIGINT, signal_handler)

# druk Ctrl+C voor melding
while True:
    print(".", end="")
    sleep(60)


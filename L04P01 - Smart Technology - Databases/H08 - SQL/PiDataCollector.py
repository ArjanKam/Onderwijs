from EmulatorGUI import GPIO
#import RPi.GPIO as GPIO
import accessDatabase
import time
SLEEP_INTERVAL = 5
INPUT_PIN1 = 5     # sluit een schakelaar aan, Let op Pullup 10K
INPUT_PIN2 = 6
INPUT_PIN3 = 13
INPUT_PIN4 = 19

def readPorts():
    val1 = GPIO.input(INPUT_PIN1)
    val2 = GPIO.input(INPUT_PIN2)
    val3 = GPIO.input(INPUT_PIN3)
    val4 = GPIO.input(INPUT_PIN4)
    value = (val1 << 3) + (val2 << 2) + (val3 << 1) + val4
    return value

def main():
    try:
        GPIO.setmode(GPIO.BCM)            # 
        GPIO.setup(INPUT_PIN1,  GPIO.IN)  # Output
        GPIO.setup(INPUT_PIN2,  GPIO.IN)
        GPIO.setup(INPUT_PIN3,  GPIO.IN)
        GPIO.setup(INPUT_PIN4,  GPIO.IN)
        
        counter = 0     
        while True:
            time.sleep( SLEEP_INTERVAL )
            portValue = readPorts()
            accessDatabase.WriteData(counter, (1, portValue))
            counter += SLEEP_INTERVAL
    finally:
        GPIO.cleanup()                        # Zet alle pinnen op LOW

if __name__ == "__main__":
    main()
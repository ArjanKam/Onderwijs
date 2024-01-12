from machine import ADC, Pin
import utime
import time

LDR_PIN = 28

ON_VALUE = 60000

LDR_ADC = ADC(Pin(LDR_PIN))
time_end = None
time_start = None

def check_reading(ldr):
    global time_start, time_end
    if ldr >= ON_VALUE:
        time_start = time.time()
    elif ldr <= 55000:
        time_end = time.time()
    if time_end != None and time_start != None:
        total = time_end - time_start
        return total
    return 0
    
def main():
    while True:
        
        ldr_value = LDR_ADC.read_u16()
        #print(ldr_value)
        
        print(ldr_value, check_reading(ldr_value))

        
        utime.sleep(1)

if __name__ == "__main__":
    #main()
    check_reading(70000)
    time.sleep(2)
    print(check_reading(30000))
    
    check_reading(70000)
    time.sleep(4)
    print(check_reading(30000))
    
    
    
    
    
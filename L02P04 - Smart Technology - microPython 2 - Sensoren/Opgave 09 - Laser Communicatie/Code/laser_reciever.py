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
        #time_start = None
        #time_end = None
        return total
    return 0

def check_character(time):
    if time >= -5 and time <=-3:
        return "_"
    elif time >= -9 and time <=-6:
        return "."
    elif time >= 2 and time <= 4:
        return " "
    elif time >=10:
        return "       "
    return None
    
def main():
    bericht = ""
    while True:
        
        ldr_value = LDR_ADC.read_u16()
        #print(ldr_value)
        
        time_ldr = check_reading(ldr_value)
        char = check_character(time_ldr)
        if char != None:
            bericht += char
            print(time_ldr, bericht)        
        utime.sleep(1)

if __name__ == "__main__":
    main()


    
    
    
    
    
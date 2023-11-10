import machine
import utime
 
analogValue = machine.ADC(26) #ADC0
 
while True:
    reading = analogValue.read_u16()     
    print("ADC: ",reading)
    utime.sleep(0.2)
    
    
    
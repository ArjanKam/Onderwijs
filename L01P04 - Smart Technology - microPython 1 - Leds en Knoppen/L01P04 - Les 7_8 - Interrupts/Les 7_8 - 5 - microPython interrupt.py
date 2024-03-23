import machine
import time

# Define the ISR (Interrupt Service Routine)
def callback_button(pin):
    led.toggle()
    
led = machine.Pin(28, machine.Pin.OUT)

# Configure an interrupt on GPIO pin 5, triggered by pin change
knop = machine.Pin(10, machine.Pin.IN)
knop.irq(trigger= machine.Pin.IRQ_RISING | machine.Pin.IRQ_FALLING,
                  handler=callback_button)
time.sleep(.1)
try:
    while True:        
        time.sleep_ms(1000) # Your main program logic here
        print("/", end = '\b')
        time.sleep_ms(1000)
        print("\\", end = '\b')
except KeyboardInterrupt:
    print("Program interrupted by user.")

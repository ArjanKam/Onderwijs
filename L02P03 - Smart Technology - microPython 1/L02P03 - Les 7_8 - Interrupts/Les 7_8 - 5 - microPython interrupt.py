import machine
import time

# Define the ISR (Interrupt Service Routine)
def pin_interrupt_handler(pin):
    print("Interrupt triggered by pin", pin)

# Configure an interrupt on GPIO pin 5, triggered by pin change
interrupt_pin = machine.Pin(5, machine.Pin.IN, machine.Pin.PULL_UP)
interrupt_pin.irq(trigger=machine.Pin.IRQ_FALLING | machine.Pin.IRQ_RISING,
                  handler=pin_interrupt_handler)

try:
    while True:        
        time.sleep_ms(100) # Your main program logic here
except KeyboardInterrupt:
    print("Program interrupted by user.")
    

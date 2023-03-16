from machine import Pin
from time import sleep

motion = False

def handle_interrupt(pin):
  global motion
  motion = True
  global interrupt_pin
  interrupt_pin = pin 

rle = Pin(12, Pin.OUT)
pir = Pin(14, Pin.IN)
knop = Pin(15, Pin.IN)

pir.irq(trigger=Pin.IRQ_RISING, handler=handle_interrupt)

rle.off()

while True:
    value = knop.value()
    if motion:
        print('Beweging gedetecteerd')
        rle.on()
        sleep(0.05)
        rle.off()
        sleep(0.2)
        rle.on()
        sleep(0.09)
        rle.off()
        sleep(0.3)
        rle.on()
        sleep(5)
        rle.off()
        print('Geen beweging gedetecteerd')
        motion = False
    if value == 1:
        print('knop aan')
        rle.on()
        sleep(0.05)
        rle.off()
        sleep(0.2)
        rle.on()
        sleep(0.09)
        rle.off()
        sleep(0.3)
        rle.on()
        sleep(5)
        rle.off()
        print('knop uit')


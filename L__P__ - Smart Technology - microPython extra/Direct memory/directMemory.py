from machine import mem32,Pin
from time import sleep_ms 
# more on https://www.i-programmer.info/programming/148-hardware/15076-the-pico-in-micropython-direct-to-the-hardware.html?start=1

PINS = (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18)
out = []
for pin in PINS:
    out.append(Pin(pin, Pin.OUT))

out[1].on()

addrSIO = 0xd0000000
while True:
    mem32[addrSIO + 0x014] = 0b11100001011 #zet deze pins aan
    sleep_ms(500)
    print(f"{mem32[0xd0000000+0x010]:>032b}")
    mem32[addrSIO + 0x018] = 0b11100000011 #zet deze pins uit
    sleep_ms(500)
    print(f"{mem32[0xd0000000+0x010]:>032b}")
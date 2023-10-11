import InternalLed_v2 as led
import distance_01b as distance

while True:
    if distance.measure() < 10:
        led.on()
    else:
        led.off()



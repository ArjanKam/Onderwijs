from machine import Timer
# type the inputs here


sleep(0.1) # Wait for USB to become ready

# numbers on the screen
NUMBER_0     = (1, 2, 3, 4, 5, 6)
NUMBER_1     = (3, 4)
NUMBER_2     = (0, 2, 3, 5, 6)
NUMBER_3     = (0, 2, 3, 4, 5)
NUMBER_4     = (0, 1, 3, 4)
NUMBER_5     = (0, 1, 2, 4, 5)
NUMBER_6     = (0, 1, 4, 5, 6)
NUMBER_7     = (2, 3, 4)
NUMBER_8     = (0, 1, 2, 3, 4, 5, 6)
NUMBER_9     = (0, 1, 2, 3, 4)
NUMBERS = (NUMBER_0, NUMBER_1, NUMBER_2, NUMBER_3, NUMBER_4, NUMBER_5, NUMBER_6, NUMBER_7, NUMBER_8, NUMBER_9)
PIN_SEGMENTS = (??, ??, ??, ??, ??, ??, ??) # vul hier de nummer in
segments = []
for pin in PIN_SEGMENTS:
  segments.append(Pin(pin, Pin.OUT))

print("Init complete !")
sleep(0.1) # Wait for USB to become ready

# toggle part, dot is the dp pin on the 7-segment display
def toggleDot(timer):
  dot.toggle()
toggleTimer = Timer()
toggleTimer.init(period=1000, mode=Timer.ONCE, callback=<vul hier de functienaam in>)

# 7 segment display part
def showValue(value:int):
  showNumber = NUMBERS[value%10]
  for x in range(7):
      if x in showNumber:
        segments[x].on()
      else:
        segments[x].off()

# main loop
counter = 0
while True:
  sleep(0.1)
  
  # type your code HERE 



import random
TOPIC = "DZHF/ARJAN/TEMPERATURE"

def whatToSend():
    return [(TOPIC, 42.3)]
#     measurement = Measure.getValue()
#     print(measurement)
#     client.publish(TOPIC, str(measurement))
 
def getMinMax():
    newValue = getValue()
    
    return minValue, maxValue
    
def getValue():
    return random.randint(20, 40)

if __name__ == "__main__":
    x = 100
    while x > 0:
        print(getValue())
        x -= 1
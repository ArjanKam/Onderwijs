import math
CSV_HEADER = "MetingId; Land; Element; Sensor; Waarde"
 
def is_float(string):
    try:
        if math.isinf(float(string)):
            return False
        return True
    except ValueError:
        return False
    
def write_to_json(topics, msg):
    None
    
metingId = 1
#topics contains 3 elements in list, msg is a string
def write_to_csv(topics, msg):
    global metingId
    if not is_float(msg):
        return
    waarde = float(msg)
    
    sensor = topics[2][7:]
    if not sensor.isnumeric():
        return
    line = f"{metingId};'{topics[0]}';'{topics[1]}';{sensor};{waarde}"
    
    f = open("demofile3.txt", "w")
    f.write(line)
    f.close()
    
    metingId += 1

if __name__ == "__main__":
    write_to_csv(("Nederland", "Temperatuur", "Sensor 1"), "2.34")
    write_to_csv(("Nederland", "Temperatuur", "Sensor hfueg"), "2.34")
    
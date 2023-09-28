import math
import os.path

CSV_HEADER = "\"MetingId\";\"Land\";\"Element\";\"Sensor\";\"Waarde\""
CSV_EXPORT_FILENAME = "EuropeTemperature.csv"
ENTER = "\n"

def is_non_zero_file(fpath):  
    return os.path.isfile(fpath) and os.path.getsize(fpath) > 0

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
    line = f"{metingId};\"{topics[0]}\";\"{topics[1]}\";{sensor};{waarde}"
    
    newFile = not is_non_zero_file(CSV_EXPORT_FILENAME)
    
    f = open(CSV_EXPORT_FILENAME, "a")
    if newFile:
        f.write(CSV_HEADER + ENTER)
    f.write(line + ENTER)
    print(line)
    f.close()
    
    metingId += 1

if __name__ == "__main__":
    write_to_csv(("Nederland", "Temperatuur", "Sensor 1"), "2.34")
    write_to_csv(("Nederland", "Temperatuur", "Sensor hfueg"), "2.34")
    write_to_csv(("Nederland", "Temperatuur", "Sensor 2"), "42.42")
    
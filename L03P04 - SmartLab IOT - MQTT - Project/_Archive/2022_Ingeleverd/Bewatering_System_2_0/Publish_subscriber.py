import paho.mqtt.client as mqtt
import time
import Logger

# static values
TOPIC = [("G7/+",0)]
#TOPIC2 = "G7/VALVE"


# Check the moisture level and send the data with MQTT to the wemos
def on_message(client, userdata, message):
    # Split the topic
    topic = message.topic.split('/')
    # Decode the moisture value
    moisture = float(message.payload.decode("utf-8"))

    # Create a data object of the values
    data = [{'Moisture': str(moisture), 'Valve': str(valve)}]
    # Save the data object in the logger
    Logger.add(data)

    # Console print system that allow you to check the values
    print(valve)
    print(f"{topic} : {moisture}")


#Logger.startup()

# Connect to the MQTT client
client = mqtt.Client("computer")
client.connect("192.168.1.99")

# Create a mqtt loop
client.loop_start()

# Subscribe to MQTT client and get the Moisture value
client.subscribe(TOPIC)
client.on_message = on_message

# A loop that allows us to wait a bit before running again
while True:
    # pass # do not use pass... too much CPU consumption
    time.sleep(10)
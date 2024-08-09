import paho.mqtt.client as mqtt
import json
import time

BROKER = 'test.mosquitto.org'
PORT = 1883
TOPIC = 'hotel/temperature'
THRESHOLD = 25.0  # Temperature threshold in Celsius
DURATION = 5  # Duration in minutes (5 data points = 5 minutes)

data_points = []

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe(TOPIC)

def on_message(client, userdata, msg):
    global data_points
    data = json.loads(msg.payload)
    temperature = data['temperature']
    timestamp = data['timestamp']
    
    # Add the new data point
    data_points.append((temperature, timestamp))
    
    # Maintain only the last `DURATION` data points
    if len(data_points) > DURATION:
        data_points.pop(0)
    
    # Check if the temperature has exceeded the threshold for the past 5 minutes
    if all(temp > THRESHOLD for temp, _ in data_points):
        print(f"ALARM! Temperature exceeded threshold: {temperature}°C for {DURATION} minutes.")
    
    # Log the data locally
    with open('temperature_log.txt', 'a') as f:
        f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestamp))} - Temperature: {temperature}°C\n")

if __name__ == '__main__':
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(BROKER, PORT, 60)
    client.loop_forever()

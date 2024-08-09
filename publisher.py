import paho.mqtt.client as mqtt
import Adafruit_DHT
import time
import json

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4  # GPIO pin where the data line is connected

BROKER = 'test.mosquitto.org'
PORT = 1883
TOPIC = 'hotel/temperature'
PUBLISH_INTERVAL = 60  # 60 seconds

def read_temperature():
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    if temperature is not None:
        return round(temperature, 2)
    else:
        print("Failed to retrieve data from the sensor")
        return None

def publish_temperature(client):
    while True:
        temperature = read_temperature()
        if temperature is not None:
            data = {'temperature': temperature, 'timestamp': int(time.time())}
            client.publish(TOPIC, json.dumps(data))
            print(f"Published: {data}")
        time.sleep(PUBLISH_INTERVAL)

if __name__ == '__main__':
    client = mqtt.Client()
    client.connect(BROKER, PORT, 60)
    publish_temperature(client)

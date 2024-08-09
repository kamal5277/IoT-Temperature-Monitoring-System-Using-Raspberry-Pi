# IoT-Temperature-Monitoring-System-Using-Raspberry-Pi
This project is an IoT-based temperature monitoring system that uses a Raspberry Pi and a DHT sensor (DHT11/DHT22) to monitor and control the temperature in a hotel room. The system ensures that room temperatures remain within an optimal range, enhancing customer comfort.

# Features
- Publisher Program: Reads data from the DHT sensor and publishes it to an MQTT broker every 60 seconds.
- Subscriber Program: Subscribes to the temperature data from the MQTT broker, checks if the temperature exceeds a threshold for 5 consecutive minutes, and logs the data locally.
- Server Program: Exposes the latest temperature data via an HTTP API.

# Hardware Requirements

- Raspberry Pi (any model with GPIO pins)
- DHT11 or DHT22 Temperature and Humidity Sensor
- Jumper wires
- Internet connection for the Raspberry Pi

# Software Requirements

- Raspberry Pi OS (or any Linux-based OS for Raspberry Pi)
- Python 3
- MQTT Broker (e.g., Mosquitto)
- Python Libraries (see `requirements.txt`)
# Installation

1. **Clone the Repository**:

   ```bash
   git clone ## Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/yourusername/raspberry-pi-iot-temperature-monitor.git
   cd raspberry-pi-iot-temperature-monitor

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/sensor-data', methods=['GET'])
def get_sensor_data():
    try:
        with open('temperature_log.txt', 'r') as f:
            lines = f.readlines()
            if lines:
                last_line = lines[-1].strip()
                timestamp, temperature = last_line.split(' - ')
                return jsonify({'timestamp': timestamp, 'temperature': temperature.split(': ')[1]})
            else:
                return jsonify({'message': 'No data available'}), 404
    except FileNotFoundError:
        return jsonify({'message': 'Log file not found'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

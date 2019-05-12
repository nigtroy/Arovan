from flask import Flask, render_template, send_from_directory, request, jsonify

import os
import uuid
import pyowm
import json

mqtt = __import__("paho-mqtt.client")

app = Flask(__name__)

@app.route("/")
def index():
	return render_template('index.html')
	
@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('css', path)
    
@app.route('/images/<path:path>')
def send_img(path):
    return send_from_directory('images', path)
    
@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)
    
@app.route("/weather")
def weather():
    owm = pyowm.OWM('456a2d5e8adb346d23b30eae0b602d6f')
    city = request.args.get('location')
    observation = owm.weather_at_place(city)
    w = observation.get_weather()
    # {'temp_kf': None, 'temp': 299.15, 'temp_min': 298.15, 'temp_max': 300.15}
    temp = w.get_temperature(unit='celsius')
    out = {"name": city, "weather": [{"description": "dummy", "icon": "dummy icon"}], "main": {"temp": temp['temp'], "temp_max": temp['temp_max'], "temp_min": temp['temp_min']}, "wind": str(w.get_wind())}
    
    # MQTT Sending code goes here...
    client = mqtt.Client("bje_client_"+ str(uuid.UUID.hex))
    client.connect("82.165.16.151")
    client.publish("UCC/mark", json.dumps(out))
    return jsonify(out)
    
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

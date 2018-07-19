from flask import Flask, render_template, send_from_directory
import paho.mqtt.client as mqtt
import os
import pyowm
import json


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
    observation = owm.weather_at_place('London,uk')
    w = observation.get_weather()
    #print('Wind: '+ str(w.get_wind()))
    #w.get_humidity()
    client = mqtt.Client("bje_client_test1")
    return json.dumps({"wind": str(w.get_wind())})
    
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

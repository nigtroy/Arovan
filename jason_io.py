from flask import Flask
from flask import Flask, render_template, send_from_directory
import paho.mqtt.client as mqtt
import os

app = Flask(__name__)

@app.route("/")
def index():
	client = mqtt.Client("bje_client_test1")
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
    
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

from flask import Flask
from flask import Flask, render_template, send_from_directory

import os

app = Flask(__name__)

@app.route("/")
def index():
	return render_template('index.html')
	
@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('css', path)
    
@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)
    
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

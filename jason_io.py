from flask import Flask
from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def index():
	return render_template('index.html')
	
@app.route('/css/<path:path>')
def send_js(path):
    return send_from_directory('css', path)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

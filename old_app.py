from flask import Flask
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
@app.route("/")
def home():
    return "Network Intrusion Detection System Backend Running"

@app.route("/status")
def status():
    return {
        "status":"Active",
        "intrusion_detected":False,
        "packets_scanned":250
    }

if __name__ == "__main__":
    app.run(debug=True)



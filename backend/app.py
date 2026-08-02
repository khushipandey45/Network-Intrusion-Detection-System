from flask import Flask
from flask_cors import CORS
from database import get_connection
app = Flask(__name__)
CORS(app)
@app.route("/")
def home():
    return "Network Intrusion Detection System Backend Running"

@app.route("/status")
def status():
    con = get_connection()
    cursor = con.cursor()

    cursor.execute("select * from logs")
    data = cursor.fetchall()

    cursor.close()
    con.close()
    return {
        "status": "Active",
        "intrusion_detected": False,
        "packets_scanned": len(data)
    }

if __name__ == "__main__":
    app.run(debug=True)
    

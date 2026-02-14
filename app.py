from flask import Flask, jsonify
import requests

app = Flask(__name__)

IP_API = "https://api.ipify.org"
IP_INFO = "http://ip-api.com/json/"

def get_info():
    ip = requests.get(IP_API, timeout=5).text.strip()
    info = requests.get(IP_INFO + ip, timeout=5).json()
    return {
        "country": info.get("country"),
        "isp": info.get("isp")
    }

@app.route("/check-ip")
def check_ip():
    return jsonify(get_info())

@app.route("/analyze")
def analyze():
    data = get_info()
    data["result"] = "VPN analysis completed"
    return jsonify(data)

app.run(host="0.0.0.0", port=5000)
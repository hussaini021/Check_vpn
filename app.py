from flask import Flask, jsonify
import requests

app = Flask(__name__)

IP_API = "https://api.ipify.org"
IP_INFO_API = "http://ip-api.com/json/"

def get_ip_info():
    ip = requests.get(IP_API, timeout=5).text.strip()
    info = requests.get(IP_INFO_API + ip, timeout=5).json()
    return {
        "country": info.get("country"),
        "isp": info.get("isp")
    }

@app.route("/")
def home():
    return "VPN Guard Pro Backend is running"

@app.route("/check-ip")
def check_ip():
    return jsonify(get_ip_info())

@app.route("/analyze")
def analyze():
    data = get_ip_info()
    data["status"] = "VPN analysis completed"
    return jsonify(data)

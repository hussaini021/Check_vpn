# 🔐 VPN Guard Pro v2.0

Advanced VPN Security Diagnostic Tool for Linux & Termux

---

## 📌 Overview

VPN Guard Pro v2.0 is a terminal-based Python tool designed to analyze the security and reliability of VPN connections.
It performs real-world tests to detect IP leaks, IPv6 exposure, proxy headers, HTTPS connectivity, and IP stability.

This project is suitable for:
- Cybersecurity students
- VPN users
- Network diagnostics
- Educational and research purposes

---

## 🚀 Features

- Public IP detection (Before & After VPN)
- Country & ISP identification
- IP stability test
- IPv6 leak detection
- Proxy / header leak detection
- HTTPS connectivity test
- Risk score calculation (0–100)
- Test history logging
- Colorful terminal UI
- Fully compatible with Termux

---

## 🖥️ Screenshot

![VPN Guard Pro](https://github.com/hussaini021/Check_vpn/blob/main/menu.png)

---

## ⚙️ Installation

### Linux / Termux
- pkg install python git -y
- pip install requests 
- git clone https://github.com/hussaini021/Check_vpn
- cd Check_vpn 
- python run.py

---

## 📂 Project Structure

Check_vpn/ ├── vpn2.py ├── data/ │   └── history.json ├── screenshots/ │   └── menu.png └── README.md

---

## 🧪 Usage

1. Run the tool: python vpn2.py

  2. Select "Run Full VPN Security Test"
3. Connect your VPN when prompted
4. View the detailed security report
5. Results are saved automatically

---

## 📊 Risk Score Logic

| Condition | Penalty |
|----------|---------|
| IP not changed | -50 |
| IPv6 leak detected | -25 |
| Proxy header leak | -25 |

Final score range: 0 (High Risk) → 100 (Low Risk)

---

## 👨‍💻 Author

Murtaza Hussaini  
University of Kabul – ISE Faculty  
3rd Year Student  

GitHub: https://github.com/hussaini021

---

## ⚠️ Disclaimer

This tool is developed for educational and research purposes only.
It does not replace professional VPN security auditing systems.

---

## 📜 License

MIT License 

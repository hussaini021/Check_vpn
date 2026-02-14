from flask import Flask, jsonify, render_template
import subprocess
import os
import sys
import threading

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PYTHON = sys.executable
RUN_FILE = os.path.join(BASE_DIR, "run.py")

analysis_output = "No analysis started yet"
analysis_status = "idle"

def run_analysis():
    global analysis_output, analysis_status
    analysis_status = "running"
    try:
        process = subprocess.Popen(
            [PYTHON, RUN_FILE],
            cwd=BASE_DIR,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        stdout, stderr = process.communicate(timeout=120)

        if stderr.strip():
            analysis_output = stderr
            analysis_status = "error"
        else:
            analysis_output = stdout
            analysis_status = "done"

    except Exception as e:
        analysis_output = str(e)
        analysis_status = "failed"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/start")
def start():
    global analysis_status
    if analysis_status == "running":
        return jsonify({"status": "running"})

    thread = threading.Thread(target=run_analysis, daemon=True)
    thread.start()
    return jsonify({"status": "started"})

@app.route("/result")
def result():
    return jsonify({
        "status": analysis_status,
        "output": analysis_output
    })            return jsonify({
                "status": "error",
                "output": stderr
            })

        return jsonify({
            "status": "success",
            "output": stdout
        })

    except subprocess.TimeoutExpired:
        process.kill()
        return jsonify({
            "status": "timeout",
            "output": "Analysis timeout (cloud limitation)"
        })

    except Exception as e:
        return jsonify({
            "status": "failed",
            "output": str(e)
        })

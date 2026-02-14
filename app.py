from flask import Flask, jsonify, render_template
import subprocess
import os
import sys

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PYTHON = sys.executable
RUN_FILE = os.path.join(BASE_DIR, "run.py")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze")
def analyze():

    if not os.path.exists(RUN_FILE):
        return jsonify({
            "status": "failed",
            "output": "run.py not found"
        })

    try:
        process = subprocess.Popen(
            [PYTHON, RUN_FILE],
            cwd=BASE_DIR,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        stdout, stderr = process.communicate(timeout=30)

        if stderr.strip():
            return jsonify({
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
            "output": "Analysis timeout (cloud environment limitation)"
        })

    except Exception as e:
        return jsonify({
            "status": "failed",
            "output": str(e)
        })

if __name__ == "__main__":
    app.run()

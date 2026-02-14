from flask import Flask, jsonify, render_template
import subprocess
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RUN_FILE = os.path.join(BASE_DIR, "run")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze")
def analyze():
    try:
        result = subprocess.run(
            [RUN_FILE],
            capture_output=True,
            text=True,
            timeout=30
        )

        if result.stderr:
            return jsonify({
                "status": "error",
                "output": result.stderr
            })

        return jsonify({
            "status": "success",
            "output": result.stdout
        })

    except Exception as e:
        return jsonify({
            "status": "failed",
            "output": str(e)
        })

if __name__ == "__main__":
    app.run()

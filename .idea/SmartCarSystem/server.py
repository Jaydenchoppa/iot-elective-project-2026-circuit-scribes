import os
os.environ["LIBCAMERA_LOG_LEVELS"] = "3"

from flask import Flask, Response, jsonify
from camera import Camera
from motor import Motor
import atexit

app = Flask(__name__)
camera = Camera()
motor = Motor()  # ✅ Motor OFF on startup

# ---------------- HOME PAGE ----------------
@app.route("/")
def home():
    return open("Website/index.html").read()

# ---------------- LIVE VIDEO ----------------
@app.route("/live")
def live():
    return Response(
        camera.generate_frames(),
        mimetype="multipart/x-mixed-replace; boundary=frame"
    )

# ---------------- SCAN FACE ----------------
@app.route("/scan", methods=["POST"])
def scan():
    result = camera.check_face()

    if result["allowed"]:
        motor.grant_access()   # ✅ Unlock — Start button enables in UI
    else:
        motor.deny_access()    # ✅ Lock and keep motor off

    return jsonify(result)

# ---------------- START ----------------
@app.route("/start", methods=["POST"])
def start():
    if motor.authorised:       # ✅ Auth check here
        motor.start()
        return jsonify({"msg": "Engine Started ✅", "started": True})
    else:
        return jsonify({"msg": "Access Denied — Scan face first ❌", "started": False})

# ---------------- STOP ----------------
@app.route("/stop", methods=["POST"])
def stop():
    motor.stop()
    return jsonify({"msg": "Engine Stopped ⛔"})

# ---------------- CLEAN EXIT ----------------
@atexit.register
def cleanup():
    motor.cleanup()

# ---------------- RUN SERVER ----------------
if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False,
        threaded=True
    )
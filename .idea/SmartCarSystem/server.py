from flask import Flask, render_template, Response, jsonify
from camera import check_face, get_frames
import motor

app = Flask(__name__, template_folder='Website')

last_scan = {"allowed": False}


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/live')
def live():
    # Stream webcam footage to the webpage
    return Response(get_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/scan', methods=['POST'])
def scan():
    global last_scan
    last_scan = check_face()
    return jsonify(last_scan)


@app.route('/start', methods=['POST'])
def start():
    if last_scan["allowed"]:
        motor.start()
        return jsonify({"msg": "Motor Started"})
    return jsonify({"msg": "Access Denied"})


@app.route('/stop', methods=['POST'])
def stop():
    motor.stop()
    return jsonify({"msg": "Motor Stopped"})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
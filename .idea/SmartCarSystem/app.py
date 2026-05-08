from flask import Flask
from flask import render_template
from flask import Response
from flask import jsonify
from flask import request

from recognition import generate_frames
from recognition import scan_face
from recognition import authorized
from recognition import detected_name
from recognition import status
from recognition import time_detected

from motorControl import start_motor
from motorControl import stop_motor

app = Flask(
    __name__,
    template_folder='Website'
)

face_result = {
    "authorized": False,
    "name": "",
    "status": "",
    "time": ""
}


@app.route('/')
def index():

    return render_template(
        'index.html'
    )


@app.route('/video_feed')
def video_feed():

    return Response(
        generate_frames(),
        mimetype='multipart/x-mixed-replace; boundary=frame'
    )


@app.route('/scan_face', methods=['POST'])
def scan():

    global face_result

    face_result = scan_face()

    return jsonify(face_result)


@app.route('/start_motor', methods=['POST'])
def start():

    if face_result["authorized"]:

        start_motor()

        return jsonify({
            "message": "Motor Started"
        })

    else:

        return jsonify({
            "message": "Access Denied"
        })


@app.route('/stop_motor', methods=['POST'])
def stop():

    stop_motor()

    return jsonify({
        "message": "Motor Stopped"
    })


if __name__ == '__main__':

    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )
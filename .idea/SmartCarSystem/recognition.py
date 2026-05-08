import cv2
from datetime import datetime

camera = cv2.VideoCapture(0)

face_detector = cv2.CascadeClassifier(
    cv2.data.haarcascades +
    "haarcascade_frontalface_default.xml"
)

recognizer = cv2.face.LBPHFaceRecognizer_create()

recognizer.read("trainer.yml")

authorized = False
detected_name = "Unknown"
status = "Waiting"
time_detected = ""


def scan_face():

    global authorized
    global detected_name
    global status
    global time_detected

    ret, frame = camera.read()

    gray = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2GRAY
    )

    faces = face_detector.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5
    )

    authorized = False

    for (x, y, w, h) in faces:

        id, confidence = recognizer.predict(
            gray[y:y+h, x:x+w]
        )

        if confidence < 60:

            authorized = True

            detected_name = "Authorized Driver"

            status = "ACCESS GRANTED"

        else:

            authorized = False

            detected_name = "Unknown Driver"

            status = "ACCESS DENIED"

        cv2.rectangle(
            frame,
            (x,y),
            (x+w,y+h),
            (0,255,0),
            2
        )

    time_detected = datetime.now().strftime(
        "%H:%M:%S"
    )

    return {
        "authorized": authorized,
        "name": detected_name,
        "status": status,
        "time": time_detected
    }


def generate_frames():

    while True:

        success, frame = camera.read()

        if not success:
            break

        ret, buffer = cv2.imencode(
            '.jpg',
            frame
        )

        frame = buffer.tobytes()

        yield (
                b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' +
                frame +
                b'\r\n'
        )
import cv2
import face_recognition
from datetime import datetime

# Load authorized face
known_image = face_recognition.load_image_file(
    "authorized_faces/driver.jpg"
)

known_encoding = face_recognition.face_encodings(
    known_image
)[0]

camera = cv2.VideoCapture(0)

authorized = False
detected_name = "Unknown"
status = "Waiting"
time_detected = ""
unknown_frame = None


def scan_face():

    global authorized
    global detected_name
    global status
    global time_detected
    global unknown_frame

    ret, frame = camera.read()

    rgb_frame = frame[:, :, ::-1]

    face_locations = face_recognition.face_locations(
        rgb_frame
    )

    face_encodings = face_recognition.face_encodings(
        rgb_frame,
        face_locations
    )

    authorized = False

    for face_encoding in face_encodings:

        matches = face_recognition.compare_faces(
            [known_encoding],
            face_encoding
        )

        if True in matches:

            authorized = True
            detected_name = "Authorized Driver"
            status = "ACCESS GRANTED"

        else:

            authorized = False
            detected_name = "Unknown Driver"
            status = "ACCESS DENIED"

            unknown_frame = frame.copy()

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

        else:

            ret, buffer = cv2.imencode(
                '.jpg',
                frame
            )

            frame = buffer.tobytes()

            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' +
                   frame +
                   b'\r\n')
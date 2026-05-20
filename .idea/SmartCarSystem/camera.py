import cv2
from datetime import datetime
from picamera2 import Picamera2

class Camera:
    def __init__(self):
        # ---------------- CAMERA ----------------
        self.picam2 = Picamera2()
        self.picam2.configure(
            self.picam2.create_preview_configuration(
                main={"format": "RGB888", "size": (320, 240)}
            )
        )
        self.picam2.start()

        # ---------------- FACE DETECTOR ----------------
        self.face_cascade = cv2.CascadeClassifier(
            "/usr/share/opencv4/haarcascades/haarcascade_frontalface_default.xml"
        )

        # ---------------- TRAINED MODEL ----------------
        self.recognizer = cv2.face.LBPHFaceRecognizer_create()
        self.recognizer.read("trainer.yml")

    # ---------------- GET FRAME ----------------
    def get_frame(self):
        frame = self.picam2.capture_array()
        return cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    # ---------------- FACE CHECK ----------------
    def check_face(self):
        frame = self.get_frame()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, 1.2, 5)

        allowed = False
        who = "Unknown"
        msg = "Access Denied"

        for (x, y, w, h) in faces:
            face = gray[y:y+h, x:x+w]
            face = cv2.resize(face, (200, 200))

            try:
                id_, score = self.recognizer.predict(face)
            except:
                continue

            print("ID:", id_, "Score:", score)

            if score < 80:
                allowed = True
                who = "Authorized Driver"
                msg = "Access Granted"

        return {
            "allowed": allowed,
            "who": who,
            "msg": msg,
            "time": datetime.now().strftime("%H:%M:%S")
        }

    # ---------------- STREAM ----------------
    def generate_frames(self):
        while True:
            frame = self.picam2.capture_array()
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            frame = cv2.resize(frame, (320, 240))
            _, buffer = cv2.imencode(".jpg", frame)
            yield (
                    b"--frame\r\n"
                    b"Content-Type: image/jpeg\r\n\r\n" +
                    buffer.tobytes() +
                    b"\r\n"
            )
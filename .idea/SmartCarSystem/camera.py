import cv2
from datetime import datetime
#import RPi.GPIO as GPIO

#IR_PIN = 27  # IR LEDs moved to pin 27

#GPIO.setmode(GPIO.BCM)
#GPIO.setup(IR_PIN, GPIO.OUT)
#GPIO.output(IR_PIN, GPIO.HIGH)  # turn LEDs on when camera starts

# Open webcam and load face tools
cam = cv2.VideoCapture(0)
finder = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
checker = cv2.face.LBPHFaceRecognizer_create()
checker.read("trainer.yml")


def check_face():
    # Take a photo from the webcam
    ok, photo = cam.read()
    gray = cv2.cvtColor(photo, cv2.COLOR_BGR2GRAY)

    # Find all faces in the photo
    faces = finder.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)

    allowed = False
    who = "Unknown"
    msg = "Access Denied"

    for (x, y, w, h) in faces:
        # Check if the face matches the trained driver
        id, score = checker.predict(gray[y:y+h, x:x+w])

        if score < 60:  # Low score = good match
            allowed = True
            who = "Authorized Driver"
            msg = "Access Granted"
        else:
            allowed = False
            who = "Unknown Driver"
            msg = "Access Denied"

        # Draw a box around the face
        cv2.rectangle(photo, (x, y), (x+w, y+h), (0, 255, 0), 2)

    now = datetime.now().strftime("%H:%M:%S")

    return {"allowed": allowed, "who": who, "msg": msg, "time": now}


def get_frames():
    # Continuously send webcam frames to the website
    while True:
        ok, photo = cam.read()
        if not ok:
            break
        ok, buf = cv2.imencode('.jpg', photo)
        yield (b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + buf.tobytes() + b'\r\n')
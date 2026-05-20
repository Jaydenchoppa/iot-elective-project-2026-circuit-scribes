import cv2
import os
import time
from picamera2 import Picamera2

name = input("Enter person's name: ")
folder = f"AuthorizedFaces/{name}"
os.makedirs(folder, exist_ok=True)

picam2 = Picamera2()
picam2.configure(picam2.create_preview_configuration(main={"format": "RGB888", "size": (320, 240)}))
picam2.start()

finder = cv2.CascadeClassifier("/usr/share/opencv4/haarcascades/haarcascade_frontalface_default.xml")

count = 0
total = 5

print(f"Capturing 5 photos for: {name}")
print("Get in front of the camera — auto capturing every 2 seconds...")
time.sleep(2)  # give time to get in position

while count < total:
    frame = picam2.capture_array()
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = finder.detectMultiScale(gray, 1.3, 5)

    if len(faces) > 0:
        count += 1
        cv2.imwrite(f"{folder}/{count}.jpg", frame)
        print(f"✅ Captured {count}/{total} — face detected")
    else:
        print("❌ No face detected — adjusting position...")

    time.sleep(2)

picam2.stop()
print(f"\nDone! Saved {count} photos for: {name}")
print("Now run train.py")
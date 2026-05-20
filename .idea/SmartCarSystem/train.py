import cv2
import numpy as np
import os

PHOTOS_FOLDER = "AuthorizedFaces"

finder = cv2.CascadeClassifier(
    "/usr/share/opencv4/haarcascades/haarcascade_frontalface_default.xml"
)

trainer = cv2.face.LBPHFaceRecognizer_create()

faces = []
labels = []
label_map = {}
current_id = 0

# ---------------- LOOP PEOPLE ----------------
for person_name in os.listdir(PHOTOS_FOLDER):
    person_path = os.path.join(PHOTOS_FOLDER, person_name)

    if not os.path.isdir(person_path):
        continue

    label_map[current_id] = person_name

    # ---------------- LOOP IMAGES ----------------
    for img_name in os.listdir(person_path):
        img_path = os.path.join(person_path, img_name)

        img = cv2.imread(img_path)
        if img is None:
            continue

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray = cv2.resize(gray, (200, 200))

        detected = finder.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in detected:
            face = gray[y:y+h, x:x+w]
            face = cv2.resize(face, (200, 200))

            if face.shape[0] < 50 or face.shape[1] < 50:
                continue

            faces.append(face)
            labels.append(current_id)

    current_id += 1

# ---------------- SAFETY CHECK ----------------
if len(faces) == 0:
    print("ERROR: No faces found in training data")
    exit()

# ---------------- TRAIN ----------------
trainer.train(faces, np.array(labels))
trainer.write("trainer.yml")

print("Training Done!")
print("People trained:", label_map)
print("Total faces:", len(faces))
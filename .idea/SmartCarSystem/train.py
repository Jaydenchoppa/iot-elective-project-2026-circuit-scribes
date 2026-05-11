import cv2
import numpy as np
from PIL import Image
import os

PHOTOS_FOLDER = 'AuthorizedFaces'

finder = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
trainer = cv2.face.LBPHFaceRecognizer_create()

faces = []
ids = []

# Loop through every photo in the folder
for filename in os.listdir(PHOTOS_FOLDER):
    path = os.path.join(PHOTOS_FOLDER, filename)

    # Open photo in grayscale
    img = np.array(Image.open(path).convert('L'), 'uint8')

    # Find faces and save them with ID 1 (one authorized driver)
    for (x, y, w, h) in finder.detectMultiScale(img):
        faces.append(img[y:y+h, x:x+w])
        ids.append(1)

# Train and save the model
trainer.train(faces, np.array(ids))
trainer.write('trainer.yml')

print("Training Done!")
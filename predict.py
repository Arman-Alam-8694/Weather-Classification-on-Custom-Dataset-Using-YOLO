from ultralytics import YOLO

import numpy as np


model = YOLO('./runs/classify/train3/weights/last.pt')  # load a custom model

results = model(r"C:\Users\arman\Downloads\70501012-fantastic-sunrise-with-cloudy-in-morning-background.jpg")  # predict on an image

names_dict = results[0].names

probs = results[0].probs.data.tolist()

print(names_dict)
print(probs)

print(names_dict[np.argmax(probs)])
import cv2

# stream
# stream = cv2.VideoCapture(0) # read from local camera
import json
labels = json.load(open("labels.json", "r"))
num_classes = len(labels) + 1
device = "cuda:0"

from SSD import *
model = Model(num_classes=num_classes, device=device)
dataset = CustomDataset("random_dir") # dataset dir does not need to be specified here if dataset.pt already exists
images = dataset.images

img_to_video_id = lambda path: path.split("/")[-1].strip(".jpg").split("-")[1]
img_to_video_frame = lambda path: path.split("/")[-1].strip(".jpg").split("-")[2]
import random
image_idx = random.choice(images) 
image = labels[image_idx]
video_filename = img_to_video_id(image)

import numpy as np
frames_paths = []
frames_idxs = []
frames_temp = []

for idx, image in images.items():
    if video_filename in image:
        frames_paths.append(image)
        frames_idxs.append(idx)
        frames_temp.append(int(img_to_video_frame(image)))

indices = np.argsort(frames_temp)
frames_paths, frames_idxs = np.array(frames_paths), np.array(frames_idxs)
frames_paths = frames_paths[indices]
frames_idxs = frames_idxs[indices]

for idx in frames_idxs:
    dataset[idx]




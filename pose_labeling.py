import cv2
from ultralytics import YOLO
import numpy as np

# Initialize YOLO model for pose detection
model = YOLO('yolov8m-pose.pt')

# Load the image
image = cv2.imread('C:/Users/Julia/Desktop/Anton/thresholding/foto.jpg')

# Perform pose detection on the image
results = model(image, show=True, conf=0.1, save=False)

# Define a dictionary mapping keypoint indices to body part names
keypoint_labels = {
    0: 'Nose',
    1: 'Left Eye',
    2: 'Right Eye',
    3: 'Left Ear',
    4: 'Right Ear',
    5: 'Left Shoulder',
    6: 'Right Shoulder',
    7: 'Left Elbow',
    8: 'Right Elbow',
    9: 'Left Wrist',
    10: 'Right Wrist',
    11: 'Left Hip',
    12: 'Right Hip',
    13: 'Left Knee',
    14: 'Right Knee',
    15: 'Left Ankle',
    16: 'Right Ankle'
}

coordinates = {}

# Draw keypoints with labels on the image
for r in results:
    print(type(r))
    #print(r.keypoints)
    for kp in zip(keypoint_labels.values(), r.keypoints[0].xy[0]):
        coordinates[kp[0]] = {"x":float(kp[1][0]),
                              "y":float(kp[1][1])
            } 
                    
print(coordinates)
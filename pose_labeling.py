import cv2
from ultralytics import YOLO
import numpy as np

# Initialize YOLO model for pose detection
model = YOLO('yolov8m-pose.pt')

# Load the image
image = cv2.imread('C:/Users/Julia/Desktop/Anton/thresholding/foto.jpg')

# Perform pose detection on the image
results = model(image, show=True, conf=0.1, save=False)

cv2.imshow('Stream', image)

cv2.destroyAllWindows()

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

coords_overview = {}
coordinates = {}

# Draw keypoints with labels on the image
for r in results:
    print(type(r))
    #print(r.keypoints)
    for kp in zip(keypoint_labels.values(), r.keypoints[0].xy[0]):
        coords_overview[kp[0]] = {"x":float(kp[1][0]),
                              "y":float(kp[1][1])
            } 
        coordinates[kp[0]] = np.array(kp[1])

r_wrist = coordinates["Right Wrist"]
r_elbow = coordinates["Right Elbow"]
r_shoulder = coordinates["Right Shoulder"]

print(r_elbow,r_wrist,r_shoulder)

upper_arm_vector = r_shoulder - r_elbow  
lower_arm_vector = r_wrist - r_elbow

print(upper_arm_vector)
print(lower_arm_vector)
# Calculate the dot product and magnitudes of the vectors
dot_product = np.dot(lower_arm_vector, upper_arm_vector)
magnitude_upper_arm = np.linalg.norm(upper_arm_vector)
magnitude_lower_arm = np.linalg.norm(lower_arm_vector)

# Calculate the cosine of the angle between the vectors
cosine_angle = dot_product / (magnitude_upper_arm * magnitude_lower_arm)

# Calculate the angle in radians and convert it to degrees
angle_radians = np.arccos(cosine_angle)
angle_degrees = np.degrees(angle_radians)

print("Angle between upper arm and lower arm:", angle_degrees)
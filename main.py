from ultralytics import YOLO
import cv2
def yolo2bbox(x,y,w,h):
    x1, y1 = x-w/2, y-h/2
    x2, y2 = x+w/2, y+h/2
    return x1, y1, x2, y2

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



model = YOLO('yolov8m-pose.pt')

results = model(source=0, show=True, conf=0.75, save=True, stream=True)

bbox_orig = None
bsize = 999999999
status_a = 'Decreasing'
status_n = 'Decreasing'
for r in results:
    for kp in zip(keypoint_labels.values(), r.keypoints[0].xy[0]):
        print(kp)
        print('-' * 40)
    x1, y1, x2, y2 = yolo2bbox(r.boxes.xywh[0][0], r.boxes.xywh[0][1], r.boxes.xywh[0][2], r.boxes.xywh[0][3])
    if bbox_orig is None:
        bbox_orig = abs(y2-y1)
    b1 = bsize
    b2 = abs(y2-y1)
    bsize = b2
    status_a = status_n
    if (b2-b1)/b1 < -0.01:
        status_n = 'Decreasing'
    elif (b2-b1)/b1 > 0.025:
        status_n = 'Increasing'
    bsize = b2
    print(status_n)
    if status_a != status_n:
        print("I just changed status")
        for kp in zip(keypoint_labels.values(), r.keypoints[0].xy[0]):
            print(kp)
            print('-' * 40)
    if status_n == 'Increasing' and abs(bbox_orig - b2) <= 3:
        print("Squat ended")
        for kp in zip(keypoint_labels.values(), r.keypoints[0].xy[0]):
            print(kp)
            print('-' * 40)
        break







from ultralytics import YOLO
from getLabelPos import getLabelPos
from transformBbox import transformBbox
from setStatus import setStatus

model = YOLO('yolov8m-pose.pt')

results = model(source=0, show=True, conf=0.75, save=True, stream=True)

bbox_orig = None
bsize = 999999999
status_a = 'Decreasing'
status_n = 'Decreasing'

for r in results:

    x1, y1, x2, y2 = transformBbox(r.boxes.xywh[0][0], r.boxes.xywh[0][1], r.boxes.xywh[0][2], r.boxes.xywh[0][3])

    # If bbox does not exist, then the squat just starts
    if bbox_orig is None:
        bbox_orig = abs(y2-y1)
        getLabelPos(r.keypoints[0].xy[0])

    bsize, b1, b2, y2, y1, status_a, status_n = setStatus(bsize, y2, y1, status_n)

    # If the direction changes, the squat is at its lowest point
    if status_a != status_n:
        print("I just changed status")
        getLabelPos(r.keypoints[0].xy[0])

    # If the direction the person is moving is upward and the bbox is basically the same, the squat ends
    if status_n == 'Increasing' and abs(bbox_orig - b2) <= 3:
        print("Squat ended")
        getLabelPos(r.keypoints[0].xy[0])
        break







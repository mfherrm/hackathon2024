from ultralytics import YOLO
import cv2
def yolo2bbox(x,y,w,h):
    x1, y1 = x-w/2, y-h/2
    x2, y2 = x+w/2, y+h/2
    return x1, y1, x2, y2

model = YOLO('yolov8m-pose.pt')

results = model(source=0, show=True, conf=0.75, save=True, stream=True)

bbox_orig = None
bsize = 999999999
status_a = 'Decreasing'
status_n = 'Decreasing'
for r in results:
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
    if status_n == 'Increasing' and abs(bbox_orig - b2) <= 3:
        print("Squat ended")
        break



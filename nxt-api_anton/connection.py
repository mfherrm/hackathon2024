import cv2
import requests
import numpy as np
from ultralytics import YOLO

# Login info
stream_url = "http://169.254.34.119/streaming/stream3/video.mjpeg"
username = "admin"
password = "sdi"

session = requests.Session()
session.auth = (username, password)

response = session.get(stream_url, stream=True)

# Model
model = YOLO('yolov8m-pose.pt')

print(response)

if response.status_code == 200:
    byte_buffer = bytes()
    
else:
    print("Your stream isn't working")

if response.status_code == 200:
    byte_buffer = bytes()
    for chunk in response.iter_content(chunk_size=1024):
        byte_buffer += chunk
        a = byte_buffer.find(b'\xff\xd8')
        b = byte_buffer.find(b'\xff\xd9')
        if a != -1 and b != -1:
            jpg = byte_buffer[a:b+2]
            byte_buffer = byte_buffer[b+2:]
            frame = cv2.imdecode(np.frombuffer(jpg, dtype=np.uint8), cv2.IMREAD_COLOR)

            # Perform object detection on the frame
            results = model(source=0, show=True, conf=0.1, save=False, verbose=True)

            cv2.imshow('Stream', frame)
            
            # Break loop by pressing 'q'
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

# Release the resources
cv2.destroyAllWindows()
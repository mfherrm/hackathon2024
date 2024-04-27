import requests
import numpy as np
import cv2

def openStream(stream_url, username, password):

    session = requests.Session()
    session.auth = (username, password)

    response = session.get(stream_url, stream=True)

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
                return frame
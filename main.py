  GNU nano 7.2                                                            test.py                                                                     
# Note to self: install through: sudo apt install python3-picamera2 python3-opencv
from picamera2 import Picamera2
import cv2
import time
import numpy as np

USBCam = False

# Try USB-Camera first:
cap = cv2.VideoCapture(1, cv2.CAP_V4L2)
#if False:
if cap.isOpened():
        # MS LifeCam Camera via USB
        USBCam = True
        cap.set(cv2.CAP_PROP_FRAME_WIDTH,320)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT,240)
        #cap.set(cv2.CAP_PROP_AUTOFOCUS, 0)
        #cap.set(cv2.CAP_PROP_FPS,60)
        print( cap.get( cv2.CAP_PROP_FRAME_WIDTH ) )
        print( cap.get( cv2.CAP_PROP_FRAME_HEIGHT ) )
else:
        #Internal PiCam
        picam2 = Picamera2()
        sensor_modes = picam2.sensor_modes
        print(sensor_modes)
        config = picam2.create_preview_configuration(
            #raw=picam2.sensor_modes[5],
            main={"size": (320, 240)},
            controls={"FrameRate":104.0}  # Set desired frame rate
        )
        picam2.configure(config)
        picam2.start()

frame_count = 0
start_time = time.time()
try:
        while True:
                if USBCam:
                        ret, frame = cap.read()
                        if not ret:
                                print("oops")
                                break
                else:
                        frame = picam2.capture_array()
                        red = frame[:,:,0]
                        frame = ((red>170) & (red>frame[:,:,1]+20) & (red>frame[:,:,2]+20) ).astype(np.uint8) * 255
                        #frame = cv2.inRange(cv2.cvtColor(frame,cv2.COLOR_RGB2HSV),np.array([5,99,99]),np.array([15,255,255]))
                        #frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
                        #frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
                cv2.imshow('Pi Camera', frame)
                frame_count += 1
                elapsed_time = time.time() - start_time
                if elapsed_time >= 1.0:
                        fps = frame_count / elapsed_time
                        print(f"FPS: {fps:.2f}")
                        frame_count = 0
                        start_time = time.time()
                if cv2.waitKey(1) & 0xFF == ord('q'):
                        break
finally:
        if USBCam:
                cap.release()
        else:
                picam2.stop()
        cv2.destroyAllWindows()

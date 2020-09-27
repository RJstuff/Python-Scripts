import cv2
import os
import numpy as np

cap = cv2.VideoCapture("SampleVideoNY.mp4")

try:
    if not os.path.exists('dataP'):
        os.makedirs('dataP')
except OSError:
    print("Error : Creating directory")

current_frame = 0

while(True):
    check,frame = cap.read()

    name = "./dataP/frame" + str(current_frame) + ".jpg"

    print("Creating...." + name)

    cv2.imwrite(name, frame)

    current_frame += 1

    key = cv2.waitKey(1)

    if key == ord('q'):
        break
    

    cap.release()

    cv2.destroyAllWindows

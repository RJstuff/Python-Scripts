import cv2
import numpy as np
#img1 = cv2.imread('vlcsnap-2014-01-20-18h51m28s254.PNG')
cap = cv2.VideoCapture(0)

ret, frame = cap.read()

cv2.imshow('image',frame)

cap.release()

cv2.waitKey(0)
cv2.destroyAllWindows()

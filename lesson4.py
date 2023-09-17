import cv2
import numpy as np

cap = cv2.VideoCapture(0)

cv2.namedWindow('frame')

while True:
    ret, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    cv2.imshow('frame', frame)
    cv2.imshow('hsv_frame', hsv_frame)

    if (cv2.waitKey(1) & 0xFF == ord('q')):
        break

cap.release()
cv2.destroyAllWindows()

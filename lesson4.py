import cv2
import numpy as np

def nothing(x):
    return

cap = cv2.VideoCapture(0)

cv2.namedWindow('frame')
cv2.namedWindow('trackbars')

cv2.createTrackbar('HL', 'trackbars', 0, 180, nothing)
cv2.createTrackbar('SL', 'trackbars', 0, 255, nothing)
cv2.createTrackbar('VL', 'trackbars', 0, 255, nothing)
cv2.createTrackbar('H', 'trackbars', 0, 180, nothing)
cv2.createTrackbar('S', 'trackbars', 0, 255, nothing)
cv2.createTrackbar('V', 'trackbars', 0, 255, nothing)

while True:
    ret, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    cv2.imshow('frame', frame)
    cv2.imshow('hsv_frame', hsv_frame)

    if (cv2.waitKey(1) & 0xFF == ord('q')):
        break

cap.release()
cv2.destroyAllWindows()
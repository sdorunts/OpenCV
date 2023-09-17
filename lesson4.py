import cv2
import numpy as np

def nothing(x):
    return

cap = cv2.VideoCapture(0)

cv2.namedWindow('frame')
cv2.namedWindow('trackbars', cv2.WINDOW_NORMAL)

cv2.createTrackbar('HL', 'trackbars', 0, 180, nothing)
cv2.createTrackbar('SL', 'trackbars', 0, 255, nothing)
cv2.createTrackbar('VL', 'trackbars', 0, 255, nothing)
cv2.createTrackbar('H', 'trackbars', 0, 180, nothing)
cv2.createTrackbar('S', 'trackbars', 0, 255, nothing)
cv2.createTrackbar('V', 'trackbars', 0, 255, nothing)

while True:
    ret, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    hl  = cv2.getTrackbarPos('HL', 'trackbars')
    sl  = cv2.getTrackbarPos('SL', 'trackbars')
    vl  = cv2.getTrackbarPos('VL', 'trackbars')
    h   = cv2.getTrackbarPos('H', 'trackbars')
    s   = cv2.getTrackbarPos('S', 'trackbars')
    v   = cv2.getTrackbarPos('V', 'trackbars')

    lower   = np.array([hl, sl, vl])
    upper   = np.array([h, s, v])
    mask    = cv2.inRange(hsv_frame, lower, upper)

    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)

    if (cv2.waitKey(1) & 0xFF == ord('q')):
        break

cap.release()
cv2.destroyAllWindows()

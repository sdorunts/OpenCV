import cv2
import numpy as np

def nothing(x):
    return

cap = cv2.VideoCapture(0)

kernel = np.ones((5, 5), np.uint8)

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

    filtered_hsv_frame = cv2.bilateralFilter(hsv_frame, 9, 75, 75)
    mask = cv2.inRange(filtered_hsv_frame, lower, upper)

    opening     = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    open_close  = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)

    edge        = cv2.Canny(open_close, 100, 200)
    contours, h = cv2.findContours(edge, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    contours    = sorted(contours, key=cv2.contourArea, reverse=True)

    for i in range(len(contours)):
        area = cv2.contourArea(contours[i])

        if (area > 300):
            x, y, w, h = cv2.boundingRect(contours[i])
            frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('open_close', open_close)

    if (cv2.waitKey(1) & 0xFF == 27):
        break


cap.release()
cv2.destroyAllWindows()

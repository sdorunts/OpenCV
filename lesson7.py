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

    blur  = cv2.blur(frame, (21, 21))
    gblur = cv2.GaussianBlur(frame, (21, 21), 0)
    bblur = cv2.bilateralFilter(frame, 21, 75, 75)

    mask    = cv2.inRange(hsv_frame, lower, upper)
    res     = cv2.bitwise_and(frame, frame, mask=mask)
    erosion = cv2.erode(mask, kernel=kernel, iterations=1)
    dilation = cv2.dilate(mask, kernel=kernel, iterations=1)
    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    open_close = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)

    cv2.imshow('frame', frame)
    # cv2.imshow('blur', blur)
    # cv2.imshow('gblur', gblur)
    # cv2.imshow('bblur', bblur)
    cv2.imshow('mask', mask)
    cv2.imshow('erosion', erosion)
    cv2.imshow('dilation', dilation)
    cv2.imshow('opening', opening)
    cv2.imshow('closing', closing)
    cv2.imshow('open_close', open_close)
    # cv2.imshow('res', res)

    if (cv2.waitKey(1) & 0xFF == 27):
        break


cap.release()
cv2.destroyAllWindows()

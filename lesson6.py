import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cv2.namedWindow('frame', cv2.WINDOW_AUTOSIZE)

while True:
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edge = cv2.Canny(gray, 70, 110)
    contours, h = cv2.findContours(edge, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)

    cv2.drawContours(frame, [contours[0]], -1, (0, 0, 255), 4)
    cv2.imshow('frame', frame)
    cv2.imshow('edge', edge)

    if (cv2.waitKey(1) & 0xFF == 27):
        break

cap.release()
cv2.destroyAllWindows()

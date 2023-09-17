import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    blur = cv2.blur(frame, (21, 21))
    gblur = cv2.GaussianBlur(frame, (21, 21), 0)
    bblur = cv2.bilateralFilter(frame, 21, 75, 75)

    cv2.imshow('frame', frame)
    cv2.imshow('blur', blur)
    cv2.imshow('gblur', gblur)
    cv2.imshow('bblur', bblur)

    if (cv2.waitKey(1) & 0xFF == 27):
        break


cap.release()
cv2.destroyAllWindows()

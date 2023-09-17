import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cv2.namedWindow('frame')

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    framex = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=5)
    framey = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=5)

    cv2.imshow('frame', frame)
    cv2.imshow('framex', framex)
    cv2.imshow('framey', framey)

    if (cv2.waitKey(1) & 0xFF == 27):
        break

cap.release()
cv2.destroyAllWindows()

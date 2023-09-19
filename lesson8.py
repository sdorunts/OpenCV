import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ret_t1, t1 = cv2.threshold(gray_frame, 127, 255, cv2.THRESH_BINARY)
    ret_t2, t2 = cv2.threshold(gray_frame, 127, 255, cv2.THRESH_BINARY_INV)
    ret_t3, t3 = cv2.threshold(gray_frame, 127, 255, cv2.THRESH_TRUNC)
    ret_t4, t4 = cv2.threshold(gray_frame, 127, 255, cv2.THRESH_TOZERO)
    ret_t5, t5 = cv2.threshold(gray_frame, 127, 255, cv2.THRESH_TOZERO_INV)

    if (ret):
        cv2.imshow('t1', t1)
        cv2.imshow('t2', t2)
        cv2.imshow('t3', t3)
        cv2.imshow('t4', t4)
        cv2.imshow('t5', t5)
        cv2.imshow('gray_frame', gray_frame)

    if (cv2.waitKey(1) & 0xFF == 27):
        break


cap.release()
cv2.destroyAllWindows()

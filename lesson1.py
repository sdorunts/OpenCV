import cv2
import numpy as np

cap = cv2.VideoCapture(0) # Web camera

while True:
    ref, frame = cap.read()
    cv2.imshow("video", frame)

    if (cv2.waitKey(1) & 0xFF == ord('q')):
        break

cap.release()
cv2.destroyAllWindows()

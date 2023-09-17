import cv2
import numpy as np

img = np.zeros((700, 700, 3), np.uint8)

img = cv2.line(img, (10, 10), (600, 600), (100, 150, 50), 5)
img = cv2.rectangle(img, (10, 10), (600, 600), (255, 0, 0), 5)
img = cv2.circle(img, (500, 450), 100, (150, 50, 100), 3)

cv2.namedWindow('image')
cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
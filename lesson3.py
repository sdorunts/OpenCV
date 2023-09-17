import cv2
import numpy as np

img1 = cv2.imread('1.png')
img2 = cv2.imread('3.webp')

r1 = cv2.resize(img1, (720, 720))
r2 = cv2.resize(img2, (720, 720))

s = cv2.addWeighted(r1, 0.2, r2, 0.2, 0)

cv2.namedWindow('add', cv2.WINDOW_NORMAL)

cv2.imshow('add', s)

cv2.waitKey(0)
import cv2
import numpy as np

img = cv2.imread("opencv_logo.png", -1) # Считываю изображение с прозрачным фоном (-1)
cv2.imshow('image_logo', img) # Вывожу изображение в окне image_logo
cv2.waitKey(0) # Бесконечно ожидаю нажатия кнопки
cv2.destroyAllWindows()

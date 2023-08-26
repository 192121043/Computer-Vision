import cv2
import numpy as np
kernel = np.ones((5, 5), np.uint8)
print(kernel)
path = "C://Users//mdshu//Pictures//Camera Roll//img blur.jpg"
img = cv2.imread(path)
img_erosion = cv2.erode(img, kernel, iterations=1)
cv2.imshow('Input', img)
cv2.imshow('Erosion', img_erosion)
cv2.waitKey(0)

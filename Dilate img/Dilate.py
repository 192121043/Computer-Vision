import cv2
import numpy as np
kernel = np.ones((5, 5), np.uint8)
print(kernel)
path = "C://Users//mdshu//Pictures//Camera Roll//img blur.jpg"
img = cv2.imread(path)
img_dilation = cv2.dilate(img, kernel, iterations=1)
cv2.imshow('Input', img)
cv2.imshow('Dilation', img_dilation)
cv2.waitKey(0)

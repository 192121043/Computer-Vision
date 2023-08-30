import cv2
import numpy as np
image_path =("C://Users//mdshu//Pictures//Camera Roll//download.png")
image = cv2.imread(image_path)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
corner_response = cv2.cornerHarris(gray_image, blockSize=2, ksize=3, k=0.04)
corner_response = cv2.dilate(corner_response, None)
threshold = 0.01 * corner_response.max()
image[corner_response > threshold] = [0, 0, 255]
cv2.imshow('Harris Corners', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
import cv2
import numpy as np
kernel = np.ones((5,5),np.uint8)
path = "C://Users//mdshu//Pictures//Camera Roll//img blur.jpg"
img = cv2.imread(path)
img = cv2.resize(img,(450,750))
cv2.imshow("image",img)
cv2.waitKey(0)
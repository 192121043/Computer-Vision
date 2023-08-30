import cv2
import numpy as np
import matplotlib.pyplot as plt
image_path = "C://Users//mdshu//Pictures//Camera Roll//img blur.jpg"
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
equalized_image = cv2.equalizeHist(image)
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')
plt.subplot(1, 2, 2)
plt.imshow(equalized_image, cmap='gray')
plt.title('Equalized Image')
plt.axis('off')
plt.tight_layout()
plt.show()
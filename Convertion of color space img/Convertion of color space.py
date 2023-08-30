import cv2
image = cv2.imread("C://Users//mdshu//Pictures//Camera Roll//cat.webp")
rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
gray_image = cv2.cvtColor(rgb_image, cv2.COLOR_RGB2GRAY)
cv2.imshow('rgb',rgb_image)
cv2.imshow('gray',gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows() 
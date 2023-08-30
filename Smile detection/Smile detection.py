import cv2
image_path = "C://Users//mdshu//Pictures//Camera Roll//Dhoni.jpg."
image = cv2.imread(image_path)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')
smiles = smile_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=20)
for (x, y, w, h) in smiles:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
cv2.imshow('Smile Detection', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
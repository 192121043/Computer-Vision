import cv2
face_cascade = cv2.CascadeClassifier("C://Users//mdshu//PycharmProjects//pythonProject3//haarcascade_frontalface_default.xml")
img = cv2.imread("C://Users//mdshu//Pictures//Camera Roll//persons.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray,1.1,5)
for (x, y, w, h) in faces:
  cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
  cv2.imshow('img', img)
  cv2.waitKey(0)
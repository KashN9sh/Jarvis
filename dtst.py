
import numpy as np
import cv2
import os

face_cascade = cv2.CascadeClassifier('C:\\Users\\Kash\\AppData\\Local\\Programs\\Python\\Python36-32\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('C:\\Kash\\AppData\\Local\\Programs\\Python\\Python36-32\\Lib\\site-packages\\cv2\\data\\haarcascade_eye.xml')
face_id = 3
cap = cv2.VideoCapture(0)
count = 0
while True:
    ret, img = cap.read()
    img = cv2.flip(img, 1)  # flip video image vertically
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        count += 1

        # Save the captured image into the datasets folder
        cv2.imwrite("F:\\Jarvis\\dataset\\User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y + h, x:x + w])

        cv2.imshow('image', img)

    k = cv2.waitKey(100) & 0xff  # Press 'ESC' for exiting video
    if k == 27:
        break
    elif count >= 100:
        break

# Do a bit of cleanup
print("\n [INFO] Exiting Program and cleanup stuff")
cap.release()
cv2.destroyAllWindows()

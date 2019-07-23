import numpy as np
import cv2
import os

face_cascade = cv2.CascadeClassifier('C:\\Users\\Kash\\AppData\\Local\\Programs\\Python\\Python36-32\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('C:\\Kash\\AppData\\Local\\Programs\\Python\\Python36-32\\Lib\\site-packages\\cv2\\data\\haarcascade_eye.xml')

recognizer =cv2.face.LBPHFaceRecognizer_create()
recognizer.read('F:\\Jarvis\\trainer\\trainer.yml')
cap = cv2.VideoCapture(0)

font = cv2.FONT_HERSHEY_SIMPLEX

id = 0

names = ['None', 'Alex', 'Klejdi', 'Romario','Shasha','Unicorn','CaMo3BaH4uK']
while True:
    putin = cv2.imread('C:\\Users\\Kash\\Desktop\\img.jpg')
    ret,img = cap.read()
    img=cv2.flip(img,1)
    #img=img+putin
    img = np.concatenate((img, putin), axis=1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(20, 20)

    )

    for (x,y,w,h) in faces:
        ret, img = cap.read()
        img = cv2.flip(img, 1)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.2,
            minNeighbors=5,
        )

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            id,confidence = recognizer.predict(gray[y:y + h, x:x + w])
            print(confidence)


            if (confidence <= 52):
                id = names[id]
                confidence = "  {0}%".format(round(100 - confidence))
            else:
                id = "unknown"
                confidence = "  {0}%".format(round(100 - confidence))

            cv2.putText(img, str(id), (x + 5, y - 5), font, 1, (0, 0, 255), 2)

        cv2.imshow('camera', img)

        k = cv2.waitKey(10) & 0xff
        if k == 27:
            break


cap.release()
cv2.destroyAllWindows()

import numpy as np
import cv2
import os

face_cascade = cv2.CascadeClassifier('Documents/Github/Jarvis/haarcascade_frontalface_default.xml')                                             #задал изображение каскада Хаара для лица
face_id = 3                                                                                                             #id совпадает с id в массиве names
cap = cv2.VideoCapture(0)                                                                                               #получаю картинку с нулевой камеры
count = 0                                                                                                               #переменная для счета снятых фото
while True:
    ret, img = cap.read()                                                                                               #считываю каждый кадр с камеры для дальнейшей обработки
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)                                                                        #перевел изображение в чб, т.к. быстрее обрабатывать
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)                                                                 #ищу лица с помощью каскадов Хаара
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)                                                      #обвожу лицо прямоугольником
        count += 1
        cv2.imwrite("Documents/Github/Jarvis/dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y + h, x:x + w])    #сохраняю фотку для дальнейшего обучения
        cv2.imshow('image', img)                                                                                        #показываю изображение с камеры

    k = cv2.waitKey(100) & 0xff                                                                                         #без этого изображение не обновляется
    if count >= 100:
        break

print("Изображения сняты")
cap.release()
cv2.destroyAllWindows()

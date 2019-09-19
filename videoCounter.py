import numpy as np
import cv2
import os

nums=0
a=1

font = cv2.FONT_HERSHEY_SIMPLEX                                                                                         #задал шрифт
face_cascade = cv2.CascadeClassifier('Documents/Github/Jarvis/haarcascade_frontalface_default.xml')                     #задал изображение каскада Хаара для лица
recognizer = cv2.face.LBPHFaceRecognizer_create()                                                                       #задал распознаватель для лица
recognizer.read('Documents/Github/Jarvis/trainer/trainer.yml')                                                          #загрузил базу данных в распознаватель(сбор лиц для обучения в файле dtst.py, а тренировка в train.py)
cap = cv2.VideoCapture(0)                                                                                               #получаю картинку с нулевой камеры

names = ['None', 'Dasha', 'Nastya', 'Romario','Romario']                                                                 #id в файле dtst-номер имени в массиве
while True:
    putin = cv2.imread('Documents/Github/Jarvis/img.jpg')                                                               #костыль чтобы не висла картинка,когда не найдено лицо
    ret,img = cap.read()
    img=img[0:720,300:980]                                                                                             #считываю каждый кадр с камеры для дальнейшей обработки
    img = np.concatenate((img, putin), axis=1)                                                                          #тот же костыль
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)                                                                        #перевел изображение в чб, т.к. быстрее обрабатывать
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)                                         #ищу лица с помощью каскадов Хаара
    for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)                          #обвожу лицо прямоугольником
            id,confidence = recognizer.predict(gray[y:y + h, x:x + w])                          #сравниваю лицо с базой данных
            #print(len(faces))
            #if(faces[0][0]==862):
                #print(1)
            if (len(faces)!=a and len(faces)!=1):
                nums+=len(faces)-a
            a=len(faces)
            print(nums)
            
            if (confidence <=40):
               id = names[id]
            else:
                id = "unknown"

            cv2.putText(img, str(id), (x + 5, y - 5),font, 1, (255, 255, 255), 2)               #помещаю текст с именем найденного лица
            img=img[0:720,0:680]                                                              #убрал Путина
            cv2.imshow('camera', img)                                                           #показываю изображение с камеры
            k = cv2.waitKey(10) & 0xff                                                          #без этого изображение не обновляется
cap.release()
cv2.destroyAllWindows()

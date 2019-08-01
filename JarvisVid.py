import speech_recognition as sr
from pygame import mixer
import numpy as np
import cv2
import paho.mqtt.client as mqttClient
from mqtt import publish,conn

font = cv2.FONT_HERSHEY_SIMPLEX                                                                 #задал шрифт
mixer.init()                                                                                    #подгрузка миксера для воспроизведения аудио
r = sr.Recognizer()                                                                             #задал переменной r значение sr.Recognizer для упрощения кода
conn()                                                                                          #функция подключения к серверу

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')                     #задал изображение каскада Хаара для лица
recognizer =cv2.face.LBPHFaceRecognizer_create()                                                #задал распознаватель для лица
recognizer.read('F:\\Jarvis\\trainer\\trainer.yml')                                             #загрузил базу данных в распознаватель(сбор лиц для обучения в файле dtst.py, а тренировка в train.py)
cap = cv2.VideoCapture(0)                                                                       #получаю картинку с нулевой камеры

names = ['None', 'Dasha', 'Nastya', 'Romario','Romario']                                        #id в файле dtst-номер имени в массиве
while True:
    putin = cv2.imread('C:\\Users\\Kash\\Desktop\\img.jpg')                                     #костыль чтобы не висла картинка,когда не найдено лицо
    ret,img = cap.read()                                                                        #считываю каждый кадр с камеры для дальнейшей обработки
    img = np.concatenate((img, putin), axis=1)                                                  #тот же костыль
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)                                                #перевел изображение в чб, т.к. быстрее обрабатывать
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)                                         #ищу лица с помощью каскадов Хаара
    for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)                          #обвожу лицо прямоугольником
            id,confidence = recognizer.predict(gray[y:y + h, x:x + w])                          #сравниваю лицо с базой данных
            if (confidence <=55):
               id = names[id]
               if id=='Romario':
                    with sr.Microphone() as source:
                        print("Скажите что-нибудь")
                        audio = r.listen(source)                                                #запись аудио для распознавания в текст
                    try:
                        a=r.recognize_google(audio, language="ru-RU")                           #задал переменной a значение распознанного аудио
                        print(a)
                        if (a == "включить" or a == "вкв" or a == "включи" or a == "ключи"):
                            publish(1)                                                          #отправляю на сервер сигнал о включении
                            mixer.music.load('on.mp3')                                          #загружаю голос
                            mixer.music.play()                                                  #проигрываю голос

                        if (a == "выключить" or a == "выключи"):
                            publish(0)                                                          #отправляю на сервер сигнал о выключении
                            mixer.music.load('off.mp3')                                         #загружаю голос
                            mixer.music.play()                                                  #проигрываю голос

                    except sr.UnknownValueError:
                        print("Робот не расслышал фразу")                                       #если фраза не понята, то робот напишет это, и опять начнет запись аудио

                    except sr.RequestError as e:
                        print("Ошибка сервиса; {0}".format(e))                                  #это будет выдано, если проблема с интернетом или сервисом распознавания

            else:
                id = "unknown"

            cv2.putText(img, str(id), (x + 5, y - 5),font, 1, (255, 255, 255), 2)               #помещаю текст с именем найденного лица
            img=img[0:640,0:640]                                                                #убрал Путина
            cv2.imshow('camera', img)                                                           #показываю изображение с камеры
            k = cv2.waitKey(1) & 0xff                                                           #без этого изображение не обновляется
cap.release()
cv2.destroyAllWindows()

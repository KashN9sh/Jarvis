import speech_recognition as sr
from pygame import mixer
import numpy as np
import cv2
import paho.mqtt.client as mqttClient

font = cv2.FONT_HERSHEY_SIMPLEX                             #задал шрифт
mixer.init()                                                #подгрузка миксера для воспроизведения аудио
r = sr.Recognizer()                                         #задал переменной r значение sr.Recognizer для упрощения кода

def publish(inf):                                           #функция для публикации в mqtt сервер
    client.connect(broker_address, port=port)               #подключение к серверу                               
    client.publish("test/sc1",inf)                          #передача данных в папку test/sc1 на сервере
    client.disconnect()                                     #отключение от сервера

broker_address= "m24.cloudmqtt.com"                         #адрес сервера
port = 	17587                                               #порт сервера
user = "fnetydgq"                                           #пользователь
password = "SEbDu7GOHR35"                                   #пароль

client = mqttClient.Client("Python")                        #создание нового клиента для сервера
client.username_pw_set(user, password=password)             #присвоение клиенту юзернейма и пароля

face_cascade = cv2.CascadeClassifier('C:\\Users\\Kash\\AppData\\Local\\Programs\\Python\\Python35\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('C:\\Users\\Kash\\AppData\\Local\\Programs\\Python\\Python35\\Lib\\site-packages\\cv2\\data\\haarcascade_eye.xml')

recognizer =cv2.face.LBPHFaceRecognizer_create()
recognizer.read('F:\\Jarvis\\trainer\\trainer.yml')
cap = cv2.VideoCapture(0)

names = ['None', 'Dasha', 'Nastya', 'Romario','Romario']
while True:
    putin = cv2.imread('C:\\Users\\Kash\\Desktop\\img.jpg')
    ret,img = cap.read()
    img = np.concatenate((img, putin), axis=1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(gray,scaleFactor=1.2,minNeighbors=5,minSize=(20, 20))

    for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            id,confidence = recognizer.predict(gray[y:y + h, x:x + w])

            if (confidence <=55):
                id = names[id]

                if id=='Romario':
                    with sr.Microphone() as source:
                        print("Скажите что-нибудь")
                        audio = r.listen(source)

                    try:
                        print(r.recognize_google(audio, language="ru-RU"))
                        a=r.recognize_google(audio, language="ru-RU")

                        if (a == "включить" or a == "вкв" or a == "включи" or a == "ключи"):
                              publish(1)                                    #отправляю на сервер сигнал о включении
                              mixer.music.load('on.mp3')                    #загружаю голос
                              mixer.music.play()                            #проигрываю голос
         
                        if (a == "выключить" or a == "выключи"):
                               publish(0)                                   #отправляю на сервер сигнал о выключении
                               mixer.music.load('off.mp3')                  #загружаю голос
                               mixer.music.play()                           #проигрываю голос

                    except sr.UnknownValueError:
                        print("Робот не расслышал фразу")
                    except sr.RequestError as e:
                        print("Ошибка сервиса; {0}".format(e))

            else:
                id = "unknown"

            cv2.putText(img, str(id), (x + 5, y - 5),font, 1, (255, 255, 255), 2)

            img=img[0:640,0:640]
            cv2.imshow('camera', img)
            k = cv2.waitKey(1) & 0xff

cap.release()
cv2.destroyAllWindows()

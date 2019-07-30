import speech_recognition as sr
from pygame import mixer
import paho.mqtt.client as mqttClient

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

while True:
    with sr.Microphone() as source:
        print("Скажите что-нибудь")
        audio = r.listen(source)                            #запись аудио для распознавания в текст
    try:  
        a=r.recognize_google(audio, language="ru-RU")       #задал переменной a значение распознанного аудио
        print(a)
        if (a == "включить" or a == "вкв" or a == "включи" or a == "ключи"):
              publish(1)                                    #отправляю на сервер сигнал о включении
              mixer.music.load('on.mp3')                    #загружаю голос
              mixer.music.play()                            #проигрываю голос
     
        if (a == "выключить" or a == "выключи"):
               publish(0)                                   #отправляю на сервер сигнал о выключении
               mixer.music.load('off.mp3')                  #загружаю голос
               mixer.music.play()                           #проигрываю голос
       
    except sr.UnknownValueError:
        print("Робот не расслышал фразу")                   #если фраза не понята, то робот напишет это, и опять начнет запись аудио
    except sr.RequestError as e:
        print("Ошибка сервиса; {0}".format(e))              #это будет выдано, если проблема с интернетом или сервисом распознавания

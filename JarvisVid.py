import datetime
import time
import webbrowser
#import bluetooth
import requests
from bs4 import BeautifulSoup
from gtts import gTTS
import speech_recognition as sr
from pygame import mixer
import numpy as np
import cv2
import os

#import bluetooth

punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

mp3_nameold = '111'
mp3_name = "1.mp3"

mixer.init()

face_cascade = cv2.CascadeClassifier('C:\\Users\\Kash\\AppData\\Local\\Programs\\Python\\Python36-32\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('C:\\Kash\\AppData\\Local\\Programs\\Python\\Python36-32\\Lib\\site-packages\\cv2\\data\\haarcascade_eye.xml')

recognizer =cv2.face.LBPHFaceRecognizer_create()
recognizer.read('F:\\Jarvis\\trainer\\trainer.yml')
cap = cv2.VideoCapture(0)

font = cv2.FONT_HERSHEY_SIMPLEX

id = 0

names = ['None', 'Dasha', 'Nastya', 'Romario','Egor']
while True:

    ret,img = cap.read()
    img=cv2.flip(img,1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(20, 20)
    )

    for (x,y,w,h) in faces:
        ret, img = cap.read()
        img = cv2.flip(img, 1)  # Flip vertically
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.2,
            minNeighbors=5,
        )

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            id,confidence = recognizer.predict(gray[y:y + h, x:x + w])

            # Check if confidence is less them 100 ==> "0" is perfect match
            if (confidence < 100):
                id = names[id]
                confidence = "  {0}%".format(round(100 - confidence))

                while id=='Romario':



                    r = sr.Recognizer()

                    with sr.Microphone() as source:
                        print("Скажите что-нибудь")
                        audio = r.listen(source)

                    try:
                        print(r.recognize_google(audio, language="ru-RU"))
                        a=r.recognize_google(audio, language="ru-RU")


                        '''if (a == "включить" or a == "вкв" or a == "включи"):
                           bd_addr = "98:D3:32:10:DE:A4"

                           port = 1

                           sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
                           sock.connect((bd_addr, port))

                           sock.send("1111")
                           sock.close()

                        if (a == "выключить" or a == "выключи"):
                        bd_addr = "98:D3:32:10:DE:A4"
                        port = 1
                        sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
                        sock.connect((bd_addr, port))
                        sock.send("0000")
                        sock.close()

                        if (a == "привет"):

                        if (b == 0):
                            print("Здравствуй, хозяин!")
                            x = "Здравствуй, хозяин!"
                            mixer.music.load("Hi.mp3")
                            mixer.music.play()

                        elif (b == 1):
                            print("Здравствуй, хозяин!")
                            x = "Здравствуй, хозяин!"
                            mixer.music.load("HI3.mp3")
                            mixer.music.play()

                        elif (b == 2):
                            print("Здравствуй, хозяин!")
                            x = "Здравствуй, хозяин!"
                            mixer.music.load("Hi2.mp3")
                            mixer.music.play()

                    if (a == "ало Сергей"):

                        if (b == 0):
                            print("Нет, меня зовут Джарвис")
                            x = "Нет, меня зовут Джарвис"
                            tts = gTTS(text=x, lang='ru')
                            tts.save(mp3_name)
                            mixer.music.load(mp3_name)
                            mixer.music.play()
                            while mixer.music.get_busy():
                                time.sleep(0.1)
                            if (os.path.exists(mp3_nameold) and (mp3_nameold != "1.mp3")):
                                os.remove(mp3_nameold)
                            mp3_nameold = mp3_name

                            mp3_name = "123" + ".mp3"

                            mixer.music.load('1.mp3')
                        if (b == 1):
                            print("Нет, меня зовут Джарвис")
                            x = "Нет, меня зовут Джарвис"
                            tts = gTTS(text=x, lang='ru')
                            tts.save(mp3_name)
                            mixer.music.load(mp3_name)
                            mixer.music.play()
                            while mixer.music.get_busy():
                                time.sleep(0.1)
                            if (os.path.exists(mp3_nameold) and (mp3_nameold != "1.mp3")):
                                os.remove(mp3_nameold)
                            mp3_nameold = mp3_name

                            mp3_name = "123" + ".mp3"

                            mixer.music.load('1.mp3')

                        elif (b == 2):
                            print("Баржа")
                            x = "Баржа"
                            tts = gTTS(text=x, lang='ru')
                            tts.save(mp3_name)
                            mixer.music.load(mp3_name)
                            mixer.music.play()
                            while mixer.music.get_busy():
                                time.sleep(0.1)
                            if (os.path.exists(mp3_nameold) and (mp3_nameold != "1.mp3")):
                                os.remove(mp3_nameold)
                            mp3_nameold = mp3_name

                            mp3_name = "123" + ".mp3"

                            mixer.music.load('1.mp3')
                    if (a == "отгони баржу"):
                        if (b == 0):
                            print("Ожидайте,хозяин")
                            x = "Ожидайте, хозяин"

                            mixer.music.load("Yes.mp3")
                            mixer.music.play()


                        elif (b == 1):
                            print("Фиг")
                            x = "Фиг"
                            mixer.music.load("Yes2.mp3")
                            mixer.music.play()


                        elif (b == 2):
                            print("Зачем?")
                            x = "Зачем?"

                            mixer.music.load("Yes3.mp3")
                            mixer.music.play()

                    if (b == 2 and a == reason):
                        print("Ок")
                        x = "Ок"
                        tts = gTTS(text=x, lang='ru')
                        tts.save(mp3_name)
                        mixer.music.load(mp3_name)
                        mixer.music.play()
                        while mixer.music.get_busy():
                            time.sleep(0.1)
                        if (os.path.exists(mp3_nameold) and (mp3_nameold != "1.mp3")):
                            os.remove(mp3_nameold)

                        mixer.music.load('1.mp3')

                    if (a == "как дела"):
                        if (b == 0):
                            print("Лучше чем у вас")
                            x = "Лучше чем у вас"
                            tts = gTTS(text=x, lang='ru')
                            tts.save(mp3_name)
                            mixer.music.load(mp3_name)
                            mixer.music.play()
                            while mixer.music.get_busy():
                                time.sleep(0.1)
                            if (os.path.exists(mp3_nameold) and (mp3_nameold != "1.mp3")):
                                os.remove(mp3_nameold)

                            mixer.music.load('1.mp3')



                        elif (b == 1):
                            print("Я глупая машина,как вы думаете,как у меня дела?")
                            x = "Я глупая машина,как вы думаете,как у меня дела?"
                            tts = gTTS(text=x, lang='ru')
                            tts.save(mp3_name)
                            mixer.music.load(mp3_name)
                            mixer.music.play()
                            while mixer.music.get_busy():
                                time.sleep(0.1)
                            if (os.path.exists(mp3_nameold) and (mp3_nameold != "1.mp3")):
                                os.remove(mp3_nameold)

                            mixer.music.load('1.mp3')

                        else:
                            print("Хорошо")
                            x = "Хорошо"

                            mixer.music.load("berda.mp3")
                            mixer.music.play()
                '''
                        if (a == "поиск"):
                            o = "Что найти?"
                            tts = gTTS(text=o, lang='ru')
                            tts.save(mp3_name)
                            mixer.music.load(mp3_name)
                            mixer.music.play()
                            while mixer.music.get_busy():
                                time.sleep(0.1)
                            if (os.path.exists(mp3_nameold) and (mp3_nameold != "1.mp3")):
                                os.remove(mp3_nameold)
                            mp3_nameold = mp3_name

                            mp3_name = "123" + ".mp3"

                            dict = ""
                            query = input('Что найти?: ')
                            url = 'http://www.google.com/search?q='
                            page = requests.get(url + query)
                            soup = BeautifulSoup(page.text)
                            h3 = soup.find_all("h3", class_="r")
                            for elem in h3:
                                elem = elem.contents[0]
                                elem = elem["href"]
                                if "wikipedia" in elem:
                                    link = ("https://www.google.com" + elem)
                                    break
                            page = requests.get(link)
                            soup = BeautifulSoup(page.text)
                            text = soup.find()
                            p = text.find("p")

                            print(page.text)

                            o = "Я нашел информацию в википедии"
                            tts = gTTS(text=o, lang='ru')
                            tts.save(mp3_name)
                            mixer.music.load(mp3_name)
                            mixer.music.play()
                            while mixer.music.get_busy():
                                time.sleep(0.1)
                            if (os.path.exists(mp3_nameold) and (mp3_nameold != "1.mp3")):
                                os.remove(mp3_nameold)
                            mp3_nameold = mp3_name

                            mp3_name = "123" + ".mp3"

                            webbrowser.open(link)

                        if (a!="поиск"):

                            phraze = a + ".txt"
                            phrase2 = a + ".mp3"

                        if (os.path.exists(phrase2) == False):
                            if (os.path.exists(phraze) == True):
                                file = open(a + ".txt", "r")
                                x = file.read()
                                tts = gTTS(text=x, lang='ru')
                                tts.save(mp3_name)
                                mixer.music.load(mp3_name)
                                mixer.music.play()
                                while mixer.music.get_busy():
                                    time.sleep(0.1)
                                if (os.path.exists(mp3_nameold) and (mp3_nameold != "1.mp3")):
                                    os.remove(mp3_nameold)
                                    mp3_nameold = mp3_name
                                    now_time = datetime.datetime.now()
                                    mp3_name = a + ".mp3"
                            else:
                                print("Научи")
                                x = "Научи"
                                tts = gTTS(text=x, lang='ru')
                                tts.save(mp3_name)
                                mixer.music.load(mp3_name)
                                mixer.music.play()
                                while mixer.music.get_busy():
                                    time.sleep(0.1)
                                if (os.path.exists(mp3_nameold) and (mp3_nameold != "1.mp3")):
                                    os.remove(mp3_nameold)
                                    mp3_nameold = mp3_name
                                    now_time = datetime.datetime.now()
                                    mp3_name = now_time.strftime("%S") + ".mp3"

                                no_punct = ""

                                file = open(a + ".txt", "w")
                                file.write(input())
                                file.close()

                                file = open(a + ".txt", "r")
                                a = file.read()

                                tts = gTTS(text=a, lang='ru')
                                tts.save(phrase2)



                        else:

                            mixer.music.load(phrase2)
                            mixer.music.play()
                            while mixer.music.get_busy():
                                time.sleep(0.1)

                    except sr.UnknownValueError:
                        print("Робот не расслышал фразу")
                    except sr.RequestError as e:
                        print("Ошибка сервиса; {0}".format(e))
            else:
                id = "unknown"
                confidence = "  {0}%".format(round(100 - confidence))

            cv2.putText(img, str(id), (x + 5, y - 5), font, 1, (255, 255, 255), 2)


        cv2.imshow('camera', img)

        k = cv2.waitKey(10) & 0xff  # Press 'ESC' for exiting video
        if k == 27:
            break


cap.release()
cv2.destroyAllWindows()

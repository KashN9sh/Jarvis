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
now_time = datetime.datetime.now()
mp3_name = now_time.strftime("%d%m%Y%I%M%S") + ".mp3"

dict = ""
query = input('What are you searching for?: ')
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
print(p)
webbrowser.open(link)


class BrickSetSpider(scrapy.Spider):
    name = "brickset_spider"
    start_urls = ['link']





 if (a!="привет" or a!="ало Сергей?" or a!="отгони баржу" or a!="как дела?" ):
     mixer.music.load(a+".mp3")
     mixer.music.play()

     if os.path.exists(r a+'.txt')









     with sr.Microphone() as source:
         print("Скажите что-нибудь")
         audio = r.listen(source)

     try:
         print(r.recognize_google(audio, language="ru-RU"))
     except sr.UnknownValueError:
         print("Робот не расслышал фразу")
     except sr.RequestError as e:
         print("Ошибка сервиса; {0}".format(e))




         my_file = open("some.txt")
         my_string = my_file.read()
         print("Было прочитано:")
         print(my_string)
         my_file.close()

         x = my_string
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
         mp3_name = now_time.strftime("%d%m%Y%I%M%S") + ".mp3"

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

         if (a == "ало Сергей?"):

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

         if (a == "как дела?"):
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

         if (a != "привет" and a != "ало Сергей?" and a != "отгони баржу" and a != "как дела?" and a != "поиск"):

             phrase = a + ".txt"

             if (os.path.exists(phrase) == False):

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
                 for char in a:
                     if char not in punctuations:
                         no_punct = no_punct + char
                 a = no_punct

                 file = open(a + ".txt", "w")
                 file.write(input())
                 file.close()



             else:
                 my_file = open(a + ".txt")
                 my_string = my_file.read()
                 print("Было прочитано:")
                 print(my_string)
                 my_file.close()

                 x = my_string
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

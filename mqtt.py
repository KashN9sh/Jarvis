import paho.mqtt.client as mqttClient
import pandas
import xlsxwriter as writer
import os.path

client = mqttClient.Client("Python")                                #создание нового клиента для сервера
data=pandas.read_excel('data.xlsx')                                 #файл с которого берутся данные сервера

class dt():                                                         #класс,который хранит данные о сервере
    broker_address= str(data.broker_adress[0])                      #адрес сервера
    port = int(data.port[0])                                        #порт сервера
    user = str(data.user[0])                                        #пользователь
    password = str(data.password[0])                                #пароль
    
def conn():                                                         #функция коннекта к серверу
    if (os.path.exists('data.xlsx')!=True):                         #создается файл с данными,если его нет
        workbook = writer.Workbook('data.xlsx')
        worksheet=workbook.add_worksheet()
        worksheet.write('A1', 'broker_adress') 
        worksheet.write('B1', 'port') 
        worksheet.write('C1', 'user') 
        worksheet.write('D1', 'password')
        workbook.close()
        print('Заполните таблицу')
    else:
        client.username_pw_set(dt.user, password=dt.password)       #присвоение клиенту юзернейма и пароля

def publish(inf):                                                   #функция для публикации в mqtt сервер
    client.connect(dt.broker_address, port=dt.port)                 #подключение к серверу                               
    client.publish("test/sc1",inf)                                  #передача данных в папку test/sc1 на сервере
    client.disconnect()                                             #отключение от сервера

    

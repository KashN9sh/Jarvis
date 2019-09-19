import cv2
import numpy as np
from PIL import Image
import os


path = 'Documents/Github/Jarvis/dataset'                                        #сюда сохранялись лица при использовании dtst.py
recognizer =cv2.face.LBPHFaceRecognizer_create()                                #задал распознаватель для лица
detector = cv2.CascadeClassifier('Documents/Github/Jarvis/haarcascade_frontalface_default.xml')         #задал изображение каскада Хаара для лица

def getImagesAndLabels(path):
    imagePaths = [os.path.join(path,f) for f in os.listdir(path)]               #считываю каждое изображение в папке
    faceSamples=[]
    ids = []
    for imagePath in imagePaths:
        PIL_img = Image.open(imagePath).convert('L')                            #перевел в чб
        img_numpy = np.array(PIL_img,'uint8')                                   #перевел изображение в массив
        id = int(os.path.split(imagePath)[-1].split(".")[1])
        faces = detector.detectMultiScale(img_numpy)                            #ищу лица
        for (x,y,w,h) in faces:
            faceSamples.append(img_numpy[y:y+h,x:x+w])
            ids.append(id)

    return faceSamples,ids

faces,ids = getImagesAndLabels(path)
recognizer.train(faces, np.array(ids))
recognizer.write('Documents/Github/Jarvis/trainer/trainer.yml')
print("Тренировка окончена")

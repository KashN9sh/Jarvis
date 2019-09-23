import numpy as np
import cv2 as cv
import time

cap=cv.VideoCapture(0)
hsv_min = np.array((0, 77, 17), np.uint8)
hsv_max = np.array((208, 255, 255), np.uint8)

while True:
    ret,img=cap.read()
    img=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    #retval,img=cv.threshold(img,4, 155, cv.THRESH_BINARY)
    img = cv.medianBlur(img,5)
    img = cv.medianBlur(img,5)
    img = cv.medianBlur(img,5)
    img = cv.medianBlur(img,5)
    img = cv.medianBlur(img,5)
    img = cv.medianBlur(img,5)
    img = cv.medianBlur(img,5)
    img = cv.medianBlur(img,5)
    img = cv.medianBlur(img,5)
    img = cv.medianBlur(img,5)
    img = cv.medianBlur(img,5)
    img = cv.medianBlur(img,5)
    img = cv.medianBlur(img,5)
    img = cv.medianBlur(img,5)
    img = cv.medianBlur(img,5)
    img = cv.medianBlur(img,5)
    img = cv.medianBlur(img,5)
    img = cv.medianBlur(img,5)
    img = cv.medianBlur(img,5)
    img = cv.medianBlur(img,5)
    img = cv.medianBlur(img,5)
    img = cv.medianBlur(img,5)
    img = cv.medianBlur(img,5)
    img = cv.medianBlur(img,5)
    img = cv.medianBlur(img,5)
    img = cv.medianBlur(img,5)
    img = cv.medianBlur(img,5)
    img = cv.medianBlur(img,5)
    img = cv.medianBlur(img,5)
    img = cv.medianBlur(img,5)
    img = cv.medianBlur(img,5)
    lap=cv.Laplacian(img,cv.CV_64F)

    cv.imshow('zrchk',lap)

    k = cv.waitKey(30) & 0xff
    if k == 27:
        break


    #res=cv.inRange(gray,0,1)
    #img=cv.imread('Documents/Github/Jarvis/1.jpg')
    #templ=cv.imread('Documents/Github/Jarvis/tample.jpg')
    #retval,templ=cv.threshold(templ,25, 155, cv.THRESH_BINARY)
    #res=cv.matchTemplate(img,templ,cv.TM_SQDIFF)
    #retval, threshold = cv.threshold(res, 255, 25, cv.THRESH_BINARY)

'''
    contours0, hierarchy = cv.findContours(res, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    for cnt in contours0:
        if len(cnt)>4:
            ellipse = cv.fitEllipse(cnt)
            M = cv.moments(cnt)
            print (M)
            #y, x = np.where(img != 0)
            cv.ellipse(img,ellipse,(255,255,255),1)
            '''
            #print((x[0], y[0]))

cap.release()
cv.destroyAllWindows()

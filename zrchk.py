import numpy as np
import cv2 as cv
import time

cap=cv.VideoCapture(0)
hsv_min = np.array((0, 77, 17), np.uint8)
hsv_max = np.array((208, 255, 255), np.uint8)

while True:
    ret,img=cap.read()
    low_red = (0, 0, 0)
    high_red = (40,40,40)
    img1 = cv.inRange(img, low_red, high_red)
    contours0, hierarchy = cv.findContours(img1.copy(), cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    for cnt in contours0:
        if len(cnt) > 4:
            ellipse = cv.fitEllipse(cnt)
            cv.ellipse(img, ellipse, (127, 0, 173), 4)
            y, x = np.where(img1 != 0)
            print((x[0], y[0]))
            time.sleep(0)
            if(y[0]<50 and x[0]<50):
                print("прыэт")

    cv.imshow('zrchk', img)
    k = cv.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv.destroyAllWindows()

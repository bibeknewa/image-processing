import numpy as np
import cv2
import serial
import time

fire_cascade = cv2.CascadeClassifier('fire_detection.xml')

cap = cv2.VideoCapture(0)
while True:
    # ser1.write('0')
    ret, img = cap.read()
    # cv2.imshow('imgorignal',img)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    fire = fire_cascade.detectMultiScale(gray, 1.1, 7)
    for (x, y, w, h) in fire:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]
        print('Fire is detected..!')


    cv2.imshow('img', img)


    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
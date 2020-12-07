#By Ayush Singh

import cv2
import numpy as np
from pyzbar.pyzbar import decode
import time
import RPi.GPIO as GPIO

#Servo X axis
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
pwm= GPIO.PWM(7, 50)

obj = False
faceCascade = cv2.CascadeClassifier("/home/pi/Resources12/haarcascade_frontalface_default.xml")
cap = cv2.VideoCapture(0)
cap.set(3, 640)  # width
cap.set(4, 480)  # height
cap.set(10, 100)  # brightness
need = 0

#barcode reading
#img = cv2.imread('/home/pi/Resources12/frame (1).png')
with open('/home/pi/Resources12/myDataFile.text') as f:
    myDataList = f.read().splitlines()

while True:

    success, img = cap.read()

    for barcode in decode(img):
        myData = barcode.data.decode('utf-8')
        print(myData)
        #The if statement will check if the the QR code is authorized. If it works, face will get detected.
        if myData in myDataList:
            myOutput = 'Authorized'
            myColor = (0, 255, 0)
            cv2.destroyWindow("Result")

            while True:
                success, img = cap.read()
                imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

                faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)

                for (x, y, w, h) in faces:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                    cv2.putText(img, myData + ' User Detected', (x - 50,y + h +50 ), cv2.FONT_HERSHEY_COMPLEX, 1,(0, 0, 0), 2)
                    cv2.rectangle(img, (x + 20 , y + 20), (x + 100, y + 10 ), (0, 0, 255), 2)

                    #Algor for x axis with ranges
                    if x == 0:
                        pwm.start(12)
                    elif x in range(1,55):
                        pwm.start(10.8)
                    elif x in range(56,110):
                        pwm.start(9.6)
                    elif x in range(111,165):
                        pwm.start(8.4)
                    elif x in range(166,220):
                        pwm.start(7.2)
                    elif x in range(221,330):
                        pwm.start(6)
                    elif x in range(331,385):
                        pwm.start(5.2)
                    elif x in range(386,440):
                        pwm.start(4.4)
                    elif x in range(441,495):
                        pwm.start(3.6)
                    elif x in range(496,549):
                        pwm.start(2.8)
                    elif x == 550:
                        pwm.start(2)

                    #print("A FACE IS DETECTED")

                    while need <1:
                        r = open("/home/pi/Resources12/database", "a")
                        r.write("\n" + myData + " " + time.ctime())
                        r.close()
                        need = need + 1
                    obj = True
                    # break

                cv2.imshow("Video", img)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

        else:
            myOutput = 'Un-Authorized'
            myColor = (0, 0, 255)

        pts = np.array([barcode.polygon], np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(img, [pts], True, myColor, 5)
        pts2 = barcode.rect
        cv2.putText(img, myOutput, (pts2[0], pts2[1]), cv2.FONT_HERSHEY_SIMPLEX,
                    0.9, myColor, 2)

    cv2.imshow('Result', img)
    cv2.waitKey(1)




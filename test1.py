import cv2
import numpy as np
obj = False
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
pwm= GPIO.PWM(7, 50)

cap = cv2.VideoCapture(0)
cap.set(3, 640)  # width
cap.set(4, 480)  # height
cap.set(10, 100)  # brightness

faceCascade = cv2.CascadeClassifier("/home/pi/Resources12/haarcascade_frontalface_default.xml")

while True:
    success, img = cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.rectangle(img, (x + 20 , y + 20), (x + 100, y + 10 ), (0, 0, 255), 2)
        cv2.putText(img, 'Face Detected', (x - 50,y + h +50 ), cv2.FONT_HERSHEY_COMPLEX, 1,(0, 0, 0), 2)
        #print("A FACE IS DETECTED")
        obj = True
        import RPi.GPIO as GPIO

        if y == 0:
            pwm.start(12)
        elif y in range(1,35):
            pwm.start(10.8)
        elif y in range(36,70):
            pwm.start(9.6)
        elif y in range(71,105):
            pwm.start(8.4)
        elif y in range(106,139):
            pwm.start(7.2)
        elif y in range(140,210):
            pwm.start(6)
        elif y in range(210,245):
            pwm.start(5.2)
        elif y in range(246,280):
            pwm.start(4.4)
        elif y in range(281,315):
            pwm.start(3.6)
        elif y in range(315,349):
            pwm.start(2.8)
        elif y == 350:
            pwm.start(2)
        print(x,y)
        # break


    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# cv2.imshow("Result", img)
# cv2.waitKey(0)
import cv2

obj = False

cap = cv2.VideoCapture(0)
cap.set(3, 640)  # width
cap.set(4, 480)  # height
cap.set(10, 100)  # brightness

faceCascade = cv2.CascadeClassifier("Resources12/haarcascade_frontalface_default.xml")
# eyeCascade = cv2.CascadeClassifier('Resources12/haarcascade_eye.xml')
# smileCascade= cv2.CascadeClassifier('Resources12/haarcascade_smile.xml')
# img = cv2.imread('Resources12/md.png')

while True:
    success, img = cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)
    # eyes = eyeCascade.detectMultiScale(imgGray, 1.1, 4)
    # smile = smileCascade.detectMultiScale(imgGray, 1.1,4)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.putText(img, 'Face Detected', (x - 50,y + h +50 ), cv2.FONT_HERSHEY_COMPLEX, 1,(0, 0, 0), 2)
        print("A FACE IS DETECTED")
        obj = True
        # break

    # for (q, e, i, u) in eyes:
    #     cv2.rectangle(img, (q, e), (q + i, e + u), (255, 0, 0), 2)

    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#
# cv2.imshow("Result", img)
# cv2.waitKey(0)


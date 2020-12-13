import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
pwm= GPIO.PWM(7, 50)

GPIO.setup(11,GPIO.OUT)
pwmy= GPIO.PWM(11,50)  #ADD TO TOGETHER CODDE pwmy

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


        if y == 0:
            pwmy.start(12)
        elif y in range(1,35):
            pwmy.start(10.8)
        elif y in range(36,70):
            pwmy.start(9.6)
        elif y in range(71,105):
            pwmy.start(8.4)
        elif y in range(106,139):
            pwmy.start(7.2)
        elif y in range(140,210):
            pwmy.start(6)
        elif y in range(210,245):
            pwmy.start(5.2)
        elif y in range(246,280):
            pwmy.start(4.4)
        elif y in range(281,315):
            pwmy.start(3.6)
        elif y in range(315,349):
            pwmy.start(2.8)
        elif y == 350:
            pwmy.start(2)
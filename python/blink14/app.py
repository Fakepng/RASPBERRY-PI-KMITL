import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(14, GPIO.OUT)
GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    sleep = 100
    if GPIO.input(21):
        sleep = 100
    else:
        sleep = 1000
    GPIO.output(14, True)
    time.sleep(sleep)
    GPIO.output(14, False)
    time.sleep(sleep)


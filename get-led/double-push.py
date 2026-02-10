import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

leds = [16, 12, 25, 17, 27, 23, 22, 24]
GPIO.setup(leds, GPIO.OUT)
GPIO.output(leds, 0)

buttons = [9, 10]
GPIO.setup(buttons, GPIO.IN)

up = 9
down = 10

num = 0

def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

sleep_time = 0.2
try:
    while True:
        if num < 0 or num > 255:
            break
        if GPIO.input(up):
            if num<255:
                num = num + 1
                time.sleep(0.2)
            else:
                num=0
            time.sleep(sleep_time)

        if GPIO.input(down):
            num = num - 1
            time.sleep(sleep_time)
        if GPIO.input(up) and GPIO.input(down):
            num = 255
            time.sleep(sleep_time)
        i=0
        for led in leds:
                GPIO.output(led, dec2bin(num)[i])
                i+=1
finally:
    GPIO.output(leds, 0)
    GPIO.cleanup()
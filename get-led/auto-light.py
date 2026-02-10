import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

led = 26

GPIO.setup(led, GPIO.OUT)

photo_pin = 6

GPIO.setup(photo_pin, GPIO.IN)

try:
    while True:
        photo_state = GPIO.input(photo_pin)
        led_state = not photo_state

        GPIO.output(led, led_state)

        time.sleep(0.1)

finally:
    GPIO.cleanup()
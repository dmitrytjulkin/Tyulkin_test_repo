import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

led = 26
GPIO.setup(led, GPIO.OUT)

unit = 6
GPIO.setup(unit, GPIO.IN)

while True:
    if (GPIO.input(unit)):
        led_state = 0
    else:
        led_state = 1
    GPIO.output(led, led_state)
    time.sleep(0.2)

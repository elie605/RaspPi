# importeren van benodigde resources
import RPi.GPIO as GPIO
import time

# Pin nummer van de LED
LED_PIN = 16
# Pin modes op BCM zetten
GPIO.setmode(GPIO.BCM)
# LED pin op output modes zetten
GPIO.setup(LED_PIN, GPIO.OUT)

##!!!!! Opdracht A B en C staan hier tussen maar zijn uitgecomment
while True:
    # LED aanzetten
    GPIO.output(LED_PIN, GPIO.HIGH)
    # time.sleep(1)
    # time.sleep(0.1)
    # Slapen/wachten voor 0.01 sec
    time.sleep(0.01)
    # LED uitztten
    GPIO.output(LED_PIN, GPIO.LOW)
    # time.sleep(1)
    # time.sleep(0.1)
    # time.sleep(2)
    time.sleep(0.01)

# importeren van benodigde resources
import RPi.GPIO as GPIO
import time

# Pin nummers van de LEDs
LED_A = 13
LED_B = 15

# Pin modes op BCM zetten
GPIO.setmode(GPIO.BCM)
# LED pin op output modes zetten
GPIO.setup(LED_A, GPIO.OUT)
GPIO.setup(LED_B, GPIO.OUT)


# Elke functie is een opdracht

def a():
    while True:
        # LED A en B aanzetten
        GPIO.output(LED_A, GPIO.HIGH)
        GPIO.output(LED_B, GPIO.HIGH)
        # Slapen/wachten voor 1 sec
        time.sleep(1)

        # LED A en B uitzetten
        GPIO.output(LED_A, GPIO.LOW)
        GPIO.output(LED_B, GPIO.LOW)
        # Slapen/wachten voor 1 sec
        time.sleep(1)


def b():
    while True:
        # LED A aanzetten
        GPIO.output(LED_A, GPIO.HIGH)
        # Slapen/wachten voor 1 sec
        time.sleep(1)
        # LED A uitzetten
        GPIO.output(LED_A, GPIO.LOW)
        # Slapen/wachten voor 1 sec
        time.sleep(1)
        # LED B aanzetten
        GPIO.output(LED_B, GPIO.HIGH)
        # Slapen/wachten voor 1 sec
        time.sleep(1)
        # LED B uitzetten
        GPIO.output(LED_B, GPIO.LOW)
        # Slapen/wachten voor 1 sec
        time.sleep(1)


def c():
    while True:
        # LED A aanzetten
        GPIO.output(LED_A, GPIO.HIGH)
        # Slapen/wachten voor 1,3 sec
        time.sleep(1.3)
        # LED A uitzetten
        GPIO.output(LED_A, GPIO.LOW)
        # Slapen/wachten voor 0,7 sec
        time.sleep(0.7)
        # LED B aanzetten
        GPIO.output(LED_B, GPIO.HIGH)
        # Slapen/wachten voor 0,8 sec
        time.sleep(0.8)
        # LED B uitzetten
        GPIO.output(LED_B, GPIO.LOW)
        # Slapen/wachten voor 1,7 sec
        time.sleep(1.7)


c()

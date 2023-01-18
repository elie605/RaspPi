# importeren van benodigde resources
import RPi.GPIO as GPIO
import time

# Pin nummers van de LEDs
LED_A = 13
LED_B = 15
# Pin nummer van de knop
BUTTON_A = 5

# Pin modes op BCM zetten
GPIO.setmode(GPIO.BCM)
# LED pin op output modes zetten
GPIO.setup(LED_A, GPIO.OUT)
GPIO.setup(LED_B, GPIO.OUT)
# De knop pin op input modes zetten en als aan beschouwen als er spanning op staat
GPIO.setup(BUTTON_A, GPIO.IN, GPIO.PUD_DOWN)

# LED A en B uitzetten
GPIO.output(LED_A, 0)
GPIO.output(LED_B, 0)


# Elke functie is een opdracht

def a():
    while True:
        # Ophalen van knop status
        buttonState = GPIO.input(BUTTON_A)
        # Als de knop is ingedrukt
        if buttonState == GPIO.HIGH:
            # LED A en B aanzetten
            GPIO.output(LED_A, GPIO.HIGH)
        else:
            # LED A en B uitzetten
            GPIO.output(LED_A, GPIO.LOW)


def b():
    while True:
        # Ophalen van knop status
        buttonState = GPIO.input(BUTTON_A)
        # Als de knop is ingedrukt
        if buttonState == GPIO.HIGH:
            # LED A en B aanzetten
            GPIO.output(LED_B, GPIO.HIGH)
            # Slapen/wachten voor 1 sec
            time.sleep(1)
            # LED A en B uitzetten
            GPIO.output(LED_B, GPIO.LOW)
            # Slapen/wachten voor 1 sec
            time.sleep(1)


def c():
    while True:
        # Ophalen van knop status
        buttonState = GPIO.input(BUTTON_A)
        # Als de knop is ingedrukt
        if buttonState == GPIO.HIGH:
            # LED B uitzetten
            GPIO.output(LED_B, GPIO.LOW)
            # LED A aanzetten
            GPIO.output(LED_A, GPIO.HIGH)
            # Slapen/wachten voor 1.3 sec
            time.sleep(1.3)
            # LED A uitzetten
            GPIO.output(LED_A, GPIO.LOW)
            # LED B aanzetten
            GPIO.output(LED_B, GPIO.HIGH)
        else:
            # LED B aanzetten
            GPIO.output(LED_B, GPIO.HIGH)
        # Slapen/wachten voor 0.7 sec
        time.sleep(0.7)


c()

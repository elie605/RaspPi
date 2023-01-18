import RPi.GPIO as GPIO
import time

INPUT_A = 11

# Pin nummers van de LEDs
LED_A = 9
LED_B = 10

onOffCounter = 0

# Pin modes op BCM zetten
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_A, GPIO.OUT)
GPIO.setup(LED_B, GPIO.OUT)

# De knop pinnen op input modes zetten en als aan beschouwen als er spanning op staat
GPIO.setup(INPUT_A, GPIO.IN, GPIO.PUD_DOWN)

while True:
    # Status van knop ophalen
    buttonStateA = GPIO.input(INPUT_A)
    # Als knop ingedrukt is en er geen cyclus bezig is
    if buttonStateA == GPIO.HIGH:
        # de status omdraaien
        if onOffCounter == 0:
            onOffCounter = 1
        else:
            onOffCounter = 0
        # 0,5 sec wachten
        time.sleep(0.5)

    #als counter 1 is
    if onOffCounter == 1:
        # De led B aan en A uit zetten
        GPIO.output(LED_A, GPIO.LOW)
        GPIO.output(LED_B, GPIO.HIGH)

    #als counter 0 is
    if onOffCounter == 0:
        # De led A aan en B uit zetten
        GPIO.output(LED_B, GPIO.LOW)
        GPIO.output(LED_A, GPIO.HIGH)


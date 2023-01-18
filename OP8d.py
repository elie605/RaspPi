import RPi.GPIO as GPIO
import time

# input pins
INPUT_A = 5
INPUT_B = 6
# led pins
LED_A = 13
LED_B = 15

# Pin modes op BCM zetten
GPIO.setmode(GPIO.BCM)

# LED pin op output modes zetten
GPIO.setup(LED_A, GPIO.OUT)
GPIO.setup(LED_B, GPIO.OUT)
# De input pinnen op input modes zetten en als aan beschouwen als er spanning op staat
GPIO.setup(INPUT_A, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(INPUT_B, GPIO.IN, GPIO.PUD_DOWN)

while True:
    #ophalen van input a en b
    buttonStateA = GPIO.input(INPUT_A)
    buttonStateB = GPIO.input(INPUT_B)
    #als input A high is zet output A op HIGH  zo niet zet ouput op low
    if buttonStateA == GPIO.HIGH:
        GPIO.output(LED_A, GPIO.HIGH)
    else:
        GPIO.output(LED_A, GPIO.LOW)
    #als input B high is zet output B op HIGH zo niet zet ouput op low
    if buttonStateB == GPIO.HIGH:
        GPIO.output(LED_B, GPIO.HIGH)
    else:
        GPIO.output(LED_B, GPIO.LOW)






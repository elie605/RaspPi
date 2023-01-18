import RPi.GPIO as GPIO
from RpiMotorLib import RpiMotorLib
import time

# Pin nummers van de knoppen
BUTTON_A = 9
BUTTON_B = 10

# Pins van servo
SERVOPINS = [6, 13, 19, 26]

# Pin modes op BCM zetten
GPIO.setmode(GPIO.BCM)

# De knop pinnen op input modes zetten en als aan beschouwen als er spanning op staat
GPIO.setup(BUTTON_A, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(BUTTON_B, GPIO.IN, GPIO.PUD_DOWN)

# Aan maken van moter met het type 28BYJ
motor = RpiMotorLib.BYJMotor("moter", "28BYJ")

# het terug geven van de huidig tijd in miliseconden
def millis():
    return time.time() * 1000


#Draai de moter de kant op die meegegeven is en met de snelheid in seconden
def turn(time, wise):
    cc = False
    if wise == "left": cc = False
    if wise == "right": cc = True
    #uitrekenen van snelheid
    x = time * 2.23 / 10000
    print(x)
    motor.motor_run(SERVOPINS,x, 1, cc, False, "half", 0)


while True:
    # De huidige tijd
    currentTime = millis()
    # Ophalen van knop A en B status
    buttonStateA = GPIO.input(BUTTON_A)
    buttonStateB = GPIO.input(BUTTON_B)

    # Als knop A ingedrukt is
    if buttonStateA == GPIO.HIGH:
        turn(5, "left")
    # Als knop B ingedrukt is
    if buttonStateB == GPIO.HIGH:
        turn(12, "right")

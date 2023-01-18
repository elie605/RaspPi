# importeren van benodigde resources
import RPi.GPIO as GPIO
import time

# Pin nummers van de knoppen
BUTTON_A = 5
BUTTON_B = 21

#pin van de servo
SERVO_PIN = 18

# Pin modes op BCM zetten
GPIO.setmode(GPIO.BCM)

# De knop pinnen op input modes zetten en als aan beschouwen als er spanning op staat
GPIO.setup(BUTTON_A, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(BUTTON_B, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(SERVO_PIN, GPIO.OUT)

# de pin van de servo op de PWM stand zetten
pwm = GPIO.PWM(SERVO_PIN, 50)
#pwm starten
pwm.start(0)

# het terug geven van de huidig tijd in miliseconden
def millis():
    return time.time() * 1000

# De huidige tijd
currentTime = millis()

# Laatste keer dat de status is veranderd van de servo
servoLastTime = millis()

servoWait = millis()

def SetAngle(angle):
    # De hoek berekenen
    duty = angle / 18 + 2
    GPIO.output(SERVO_PIN, True)
    # De hoek van de servo zetten
    pwm.ChangeDutyCycle(duty)

# Houden bij of de servo aan het draaien is
# Aan het heen draaien status
TurningA = False
# Aan het terug draaien status
TurningB = False

while True:
    # Ophalen huidige tijd
    currentTime = millis()
    # Ophalen van knop A status
    buttonStateA = GPIO.input(BUTTON_A)
    # Ophalen van knop B status
    buttonStateB = GPIO.input(BUTTON_B)

    global timingp
    # Als knop A ingedrukt is
    if buttonStateA == GPIO.HIGH:
        #Als niet aan het draaien
        if not TurningA:
            #Draaien
            TurningA = True
            # De laatste keer van verandering van status op huidige tijd zetten
            servoLastTime = millis()
            #Lengte van draai
            timing = 1000

    # Als knop B ingedrukt is
    if buttonStateB == GPIO.HIGH:
        #Als niet aan het draaien
        if not TurningA:
            #Draaien
            TurningA = True
            # De laatste keer van verandering van status op huidige tijd zetten
            servoLastTime = millis()
            #Lengte van draai
            timing = 500

    # Als status van heen draaien waar is
    if TurningA:
        # Als status van terug draai niet waar is
        if not TurningB:
            # Als de huidge tijd - de laatste keer dat servo van status veranderd is meer of gelijk is dan de huidige timing
            if (currentTime - servoLastTime) >= timing:
                # De laatste keer van verandering van status op huidige tijd zetten
                servoLastTime = millis()
                SetAngle(120)
                # Terug draaien
                TurningB = True
        if TurningB:
            # Als de huidge tijd - de laatste keer dat servo van status veranderd is meer of gelijk is dan de huidige timing
            if (currentTime - servoLastTime) >= timing:
                SetAngle(0)
                #status van terug en heen draai op niet waar
                TurningB = False
                TurningA = False

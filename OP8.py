import RPi.GPIO as GPIO
import time

# Pin nummers van de LEDs
LED_A = 11
LED_B = 10

# Pin modes op BCM zetten
GPIO.setmode(GPIO.BCM)
# LED pin op output modes zetten
GPIO.setup(LED_A, GPIO.OUT)
GPIO.setup(LED_B, GPIO.OUT)


def millis():
    return time.time() * 1000


currentTime = millis()
lastTimeA = millis()
lastTimeB = millis()

lastStatusA = 0
# Voor opdracht A
lastStatusB = 1


# Voor opdracht B
# lastStatusB = 0

# Terug geven van lastStatus en vervolgens de waarde naar veranderen naar het tegen overgestelde
def getstatusa():
    global lastStatusA
    if lastStatusA == 1:
        lastStatusA = 0
        return 1
    else:
        lastStatusA = 1
        return 0


# Terug geven van lastStatus en vervolgens de waarde naar veranderen naar het tegen overgestelde
def getstatusb():
    global lastStatusB
    if lastStatusB == 1:
        lastStatusB = 0
        return 1
    else:
        lastStatusB = 1
        return 0


def a():
    global lastTimeA
    # Als de huidge tijd - de laatste keer dat LED van status veranderd is meer of gelijk is dan 3 sec
    if (currenttime - lastTimeA) >= timings[1]:
        # De laatste keer van verandering van status op huidige tijd zetten
        lastTimeA = millis()
        # De led op aan of uit zetten
        GPIO.output(LED_A, getstatusa())
        # De led op aan of uit zetten
        GPIO.output(LED_B, getstatusb())


def b():
    global lastTimeA, lastTimeB
    # Als de huidge tijd - de laatste keer dat LED van status veranderd is meer of gelijk is dan 3 sec
    if (currenttime - lastTimeA) >= timings[1]:
        # De laatste keer van verandering van status op huidige tijd zetten
        lastTimeA = millis()
        # De led op aan of uit zetten
        GPIO.output(LED_A, getstatusa())
    # Als de huidge tijd - de laatste keer dat LED van status veranderd is meer of gelijk is dan 1 sec
    if (currenttime - lastTimeB) >= timings[0]:
        # De laatste keer van verandering van status op huidige tijd zetten
        lastTimeB = millis()
        # De led op aan of uit zetten
        GPIO.output(LED_B, getstatusb())


timings = [3000, 1000]
while True:
    currenttime = millis()
    a()

import RPi.GPIO as GPIO
import time

# Led pins
ledPins = [26, 19, 13, 6]
# Input pins
inputPins = [22, 27, 17, 4]
# Verschillende timings
timings = [100, 300, 500, 700]

GPIO.setmode(GPIO.BCM)

# voor elke led pin de modes op output zetten
for pin in ledPins:
    GPIO.setup(pin, GPIO.OUT)

# voor elke input pin de modes op input zetten
for pin in inputPins:
    GPIO.setup(pin, GPIO.IN, GPIO.PUD_DOWN)

# Laatste keer dat de LED aan/uit is gegeaan
lastTimes = [0, 0, 0, 0]
# niet gebruikt, maar durf ik niet te verwijderen
lastInputFlag = [0, 0, 0, 0]
# Laatste input
lastInput = -1
# Huidige status van leds
ledStatus = [GPIO.LOW, GPIO.LOW, GPIO.LOW, GPIO.LOW]
# De snelheid waarop de led moet flikkeren
ledTiming = [0, 0, 0, 0]
# De geschiedenis van de LED die aangegeaan zijn
ledHistory = [0, 0, 0, 0]
# niet gebruikt, maar durf ik niet te verwijderen
selectedLed = -1


def millis():
    return time.time() * 1000

#update van led status en timing
def update(l, t):
    # niet gebruikt, maar durf ik niet te verwijderen
    global selectedLed
    selectedLed = -1
    # print("\n led: ", l, "\t string: ", t, "\n")
    # als led uit is
    if ledHistory[l] == 0:
        ic = 0
        for i in ledHistory:
            # de langste knipperende led uit zetten
            if i == 2:
                ledStatus[ic] = GPIO.LOW
                ledHistory[ic] = 0
                GPIO.output(ledPins[ic], GPIO.LOW)
            # de 2e langste knipperende op langst knipperende zetten
            if i == 1:
                ledHistory[ic] = 2
            ic += 1
        # de geselecteerde led op 2e langste knipperende zetten
        ledStatus[l] = GPIO.HIGH
        ledHistory[l] = 1
        GPIO.output(ledPins[l], GPIO.HIGH)

    # Timing van de geselecteerde let zetten
    ledTiming[l] = timings[t]
    roll(l)


# led knipper functie
def roll(l):
    curTime = millis()

    # Als de huidge tijd - de laatste keer dat LED van status veranderd is meer of gelijk is dan zijn timing
    # En het aan als het aan mag
    if curTime - lastTimes[l] >= ledTiming[l] and ledHistory[l] >= 1:
        # De laatste keer van verandering van status op huidige tijd zetten
        lastTimes[l] = curTime
        # led aan of uit zetten
        if ledStatus[l] == GPIO.LOW:
            ledStatus[l] = GPIO.HIGH
        else:
            ledStatus[l] = GPIO.LOW
        GPIO.output(ledPins[l], ledStatus[l])


# De input omzetten naar een update opdracht
def input(i):
    global lastInput
    global lastInputFlag
    # Status van input pin
    state = GPIO.input(inputPins[i])
    # Als die pin aan is
    if state == GPIO.HIGH:
        # Als er al een LED geslecteerd was
        if lastInput > -1:
            # Voor update uit met geselecteerde led en index van snelheid
            update(lastInput, i)
            # De laatste geslecteerde led verwijderen
            lastInput = -1
            # niet gebruikt, maar durf ik niet te verwijderen
            lastInputFlag = [0, 0, 0, 0]
        else:
            lastInput = i
            # niet gebruikt, maar durf ik niet te verwijderen
            lastInputFlag[i] = 1


update(0, 0)
update(1, 0)

while True:
    #Voor elke led
    for t in range(4):
        roll(t)
        input(t)
    time.sleep(0.1)

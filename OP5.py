# importeren van benodigde resources
import RPi.GPIO as GPIO
import time

# Pin nummers van de LEDs
LED_A = 13
LED_B = 15
# Pin nummers van de knoppen
BUTTON_A = 5
BUTTON_B = 21

# Pin modes op BCM zetten
GPIO.setmode(GPIO.BCM)
# LED pin op output modes zetten
GPIO.setup(LED_A, GPIO.OUT)
GPIO.setup(LED_B, GPIO.OUT)
# De knop pinnen op input modes zetten en als aan beschouwen als er spanning op staat
GPIO.setup(BUTTON_A, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(BUTTON_B, GPIO.IN, GPIO.PUD_DOWN)

# LED A en B uitzetten
GPIO.output(LED_A, 0)
GPIO.output(LED_B, 0)


# Elke functie is een opdracht

# het terug geven van de huidig tijd in miliseconden
def millis():
    return time.time() * 1000


# De huidige tijd
currentTime = millis()

# Laatste keer dat de status is veranderd van led
lastTimeA = millis()
lastTimeB = millis()

# Laatste status van de LED's op uit zetten
lastStatusA = 0
lastStatusB = 0

# Is/moet er een cyclus gedraaid worden
cycle = False


# Terug geven van lastStatus en vervolgens de waarde naar veranderen naar het tegen overgestelde
def getstatusa():
    global lastStatusA
    global cycle
    if lastStatusA == 1:
        lastStatusA = 0
        return 1
    else:
        lastStatusA = 1
        cycle = False
        return 0


# Terug geven van lastStatus en vervolgens de waarde naar veranderen naar het tegen overgestelde
def getstatusb():
    global lastStatusB
    global cycle
    if lastStatusB == 1:
        lastStatusB = 0
        return 1
    else:
        lastStatusB = 1
        cycle = False
        return 0


def a():
    global cycle, lastTimeA
    while True:
        # Huidige tijd
        currenttime = millis()
        # Ophalen van knop A status
        buttonState = GPIO.input(BUTTON_A)
        # Als knop ingedrukt is en er geen cyclus bezig is
        if buttonState == GPIO.HIGH and not cycle:
            # start cyclus
            cycle = True
        # Als de huidge tijd - de laatste keer dat LED van status veranderd is meer of gelijk is dan 1 sec
        # En als er een cyclus bezig is
        if (currenttime - lastTimeA) >= 1000 and cycle:
            # De laatste keer van verandering van status op huidige tijd zetten
            lastTimeA = millis()
            # De led op aan of uit zetten
            GPIO.output(LED_A, getstatusa())


def b():
    while True:
        global cycle, lastTimeA
        while True:
            # Huidige tijd
            currenttime = millis()
            # Ophalen van knop A status
            buttonState = GPIO.input(BUTTON_A)
            # Als knop ingedrukt is en er geen cyclus bezig is
            if buttonState == GPIO.HIGH and not cycle:
                # start cyclus
                cycle = True
            # Als de huidge tijd - de laatste keer dat LED van status veranderd is meer of gelijk is dan 0.7 sec
            # En als er een cyclus bezig is
            if (currenttime - lastTimeA) >= 700 and cycle:
                # De laatste keer van verandering van status op huidige tijd zetten
                lastTimeA = millis()
                # De led op aan of uit zetten
                GPIO.output(LED_A, getstatusa())


buttonStateB = 0


def c():
    # De A led aanzetten en de B led status op uit zetten
    # zodat ze tegenovergesteld zijn
    GPIO.output(LED_A, getstatusb())
    # De stand van de knop bij houden
    lastButton = 0
    global cycle, lastTimeA

    while True:
        # Huidige tijd
        currenttime = millis()
        # De verschillende timings
        timings = [[1000, 1000], [700, 1300]]

        buttonStateA = GPIO.input(BUTTON_A)
        # Als knop ingedrukt is en er geen cyclus bezig is
        if buttonStateA == GPIO.HIGH:
            #Knop stand op 1 zetten
            lastButton = 1
        else:
            #Knop stand op 0 zetten
            lastButton = 0

        # Als de huidge tijd - de laatste keer dat LED van status veranderd is meer of gelijk is dan de huidige timing
        # De huidige timing is de gebaseerd op de stand van de knop en dan de stand van led A
        if (currenttime - lastTimeA) >= timings[lastButton][lastStatusA]:
            # De laatste keer van verandering van status op huidige tijd zetten
            lastTimeA = millis()
            # De led op aan of uit zetten
            GPIO.output(LED_A, getstatusa())
            # De led op aan of uit zetten
            GPIO.output(LED_B, getstatusb())


c()

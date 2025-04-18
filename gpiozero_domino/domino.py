from gpiozero import LEDBoard,Button
from signal import pause
from time import sleep

leds=LEDBoard(8,7,16,20)
button=Button(25)

def led_domino():
        for led in leds:
            led.on()
            sleep(1)
            led.off()

button.when_pressed=led_domino

pause()
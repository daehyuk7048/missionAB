from gpiozero import LEDBoard, Button
from signal import pause

leds = LEDBoard(8, 7, 16, 20)
button = Button(25)

button.when_pressed = lambda: leds.blink(on_time=1, off_time=1, n=1)

pause()

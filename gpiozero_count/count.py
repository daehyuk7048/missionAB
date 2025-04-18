from gpiozero import LEDBoard, Button
from signal import pause

leds = LEDBoard(8, 7, 16, 20)
button = Button(25)
count = 0

def led_4bitcount():
    global count
    count = (count + 1) & 0x0F
    leds.value = tuple((count >> i) & 1 for i in range(4))

button.when_pressed = led_4bitcount
pause()
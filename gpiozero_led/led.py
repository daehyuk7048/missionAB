from gpiozero import LEDBoard,Button
from signal import pause

led1=LEDBoard(8,7,16,20)
button=Button(25)

button.when_pressed= lambda: led1.on()
button.when_released= lambda: led1.off()

pause()
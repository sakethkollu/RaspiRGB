from gpiozero import LED
from time import sleep
import keyboard

red = LED(17)
green = LED(22)
blue = LED(24)

while True:
    try:
        if keyboard.is_pressed('r'):
            red.on()
            break
        else:
            red.off()
    except:
        break
from gpiozero import LED
from time import sleep

red = LED(17)
green = LED(22)
blue = LED(24)

red.on()
green.on()
blue.on()
import board
import busio
import displayio
import digitalio
import terminalio
import time
import utime
from adafruit_display_text import label
from fourwire import FourWire
from adafruit_st7789 import ST7789

# Configuration du bouton
button1 = digitalio.DigitalInOut(board.GP14)
button1.direction = digitalio.Direction.INPUT
button1.pull = digitalio.Pull.UP

def on_button_pressed(pin):
    print("Bouton pressé !")

button1.irq(trigger=Pin.IRQ_RISING, handler=on_button_pressed)

while True:
    utime.sleep(1)  # La boucle tourne en fond, mais la fonction d'interruption s'exécute seule

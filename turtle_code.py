import board
import busio
import displayio
from adafruit_turtle import Color, turtle
from fourwire import FourWire
from adafruit_st7789 import ST7789
import time

# Release any resources currently in use for the displays
displayio.release_displays()

# SPI initialization
spi = busio.SPI(clock=board.GP18, MOSI=board.GP19)

tft_cs = board.GP27  # Pin for chip select
tft_dc = board.GP21  # Pin for Data/Command

# SPI Connection with Screen
display_bus = FourWire(spi, command=tft_dc, chip_select=tft_cs, reset=board.GP20)

# ST7789 Screen Initialization
display = ST7789(display_bus, width=320, height=240, rotation=90)

# Create group for display
splash = displayio.Group()
display.root_group = splash

# Creating the turtle
turtle = turtle(display)
turtle.pencolor(Color.WHITE)  # Pen color in white

# Initialization of the position
turtle.penup()
turtle.goto(0, 0)  # Starting position
turtle.pendown()

# Function to change pen color
def change_color(color_name):
    colors = {
        "red": Color.RED,
        "green": Color.GREEN,
        "blue": Color.BLUE,
        "yellow": Color.YELLOW,
        "orange": Color.ORANGE,
        "violet": Color.PURPLE,
        "white": Color.WHITE,
        "black": Color.BLACK
    }
    if color_name in colors:
        turtle.pencolor(colors[color_name])  # Change the color
    else:
        print(f"Color '{color_name}' not recognized, pen still untouched.")

# Fonction to deal with keyboard inputs
def control_turtle():
    while True:
        # Read keyboard inputs
        char = input("Press a key ('q' for pen down, 'e' for pen up, 'w', 'a', 's', 'd' to move, 'red', 'green', 'blue' for color, 'x' to quit) : ")

        if char == 'q':  # pen down
            turtle.pendown()
        elif char == 'e':  # pen up
            turtle.penup()
        elif char == 'w':  # move up
            turtle.setheading(90)
            turtle.forward(10)
        elif char == 'a':  # move left
            turtle.setheading(180)
            turtle.forward(10)
        elif char == 's':  # move down
            turtle.setheading(270)
            turtle.forward(10)
        elif char == 'd':  # move right
            turtle.setheading(0)
            turtle.forward(10)
        elif char == 'x':  # Quit
            break
        elif char in ["red", "green", "blue", "yellow", "orange", "violet", "white", "black"]:
            change_color(char)  # Change the pen color
        else:
            print("Unkown command. Try again.")

        time.sleep(0.1)

# Start the turtle control
control_turtle()

while True:
    pass

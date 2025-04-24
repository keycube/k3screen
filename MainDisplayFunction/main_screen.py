import board
import displayio
from adafruit_display_text import label
from adafruit_display_shapes.rect import Rect
import terminalio
import keypad
import time
import sys
import ExImg
import ExFont

def run_mainScreen(display):
    # Initialisation de l'affichage
    group = displayio.Group()
    # Création des cubes
    cubes = [
        create_cube(30, 60, "testImg", 1),
        create_cube(110, 60, "TestFont", 1),
        create_cube(190, 60, "cube3", 1)
    ]

    for cube in cubes:
        group.append(cube)

    display.root_group = group
    file_to_launch = choose_cube(display, group,cubes)
    if file_to_launch % len(cubes) == 0:
        ExImg.run_imgTest(display)
    if file_to_launch % len(cubes) == 1:
        ExFont.testFont(display)

def create_cube(x, y, text, border):
    cube = displayio.Group()
    rect = Rect(x=x, y=y, width=50, height=50, outline=0xFFFFFF, stroke=border)
    text_label = label.Label(terminalio.FONT, text=text, color=0xFFFFFF, x=x+10, y=y+20)
    cube.append(rect)
    cube.append(text_label)
    return cube

#use the inputs to write
def choose_cube(display, group,cubes):
    selected_index = 0
    cubes[selected_index][0].fill = 0xFFFFFF  # Le premier cube a un contour épais
    while True:
        # input
        try:
            input_char = sys.stdin.read(1)

            if input_char in ['\r', '\n']:  # enter to stop
                break
            elif input_char == '\x03':  # Ctrl+C to stop
                break
            if input_char == '\x1b':  # Début d'une séquence d'échappement (flèche)
                next_chars = sys.stdin.read(2)  # Lire les 2 caractères suivants
                if next_chars == '[C':
                    print("droite")
                    cubes[selected_index][0].fill = 0x000000  # Le premier cube a un contour épais
                    selected_index = (selected_index + 1) % len(cubes)
                    cubes[selected_index][0].fill = 0xFFFFFF  # Le premier cube a un contour épais

                elif next_chars == '[D':
                    print("gauche")
                    cubes[selected_index][0].fill = 0x000000  # Le premier cube a un contour épais
                    selected_index = (selected_index - 1) % len(cubes)
                    cubes[selected_index][0].fill = 0xFFFFFF  # Le premier cube a un contour épais
            display.refresh()

            time.sleep(0.1)

        except KeyboardInterrupt:
            break
    return selected_index

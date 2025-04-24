import displayio
import sys
from adafruit_display_text import label
import time
import login
import main_screen
from constants import X_MAX, Y_MAX, FONT
#display function wich launch other function
def run_welcomeScreen(display):
    image = displayio.OnDiskBitmap("dog.bmp")
    tile_grid = displayio.TileGrid(image, pixel_shader=getattr(image, 'pixel_shader', displayio.ColorConverter()))
    groupIMG = displayio.Group()  # create to group for the display
    groupTXT = displayio.Group()
    display.root_group = groupIMG
    groupIMG.append(tile_grid)
    text_name = label.Label(FONT, text="Veuillez entrer votre nom:", color=0xFFFFFF, x=125, y=50)
    groupTXT.append(text_name)
    display.refresh()
    loadNames(display, groupTXT)
    display.root_group = groupTXT
    name = writeName(display, groupTXT)
    #erase all the screen
    while len(groupTXT) > 0:
        groupTXT.pop()
    text_welcome = label.Label(FONT, text=f"Bienvenue: {name}", color=0xFFFFFF, x=125, y=75)
    groupTXT.append(text_welcome)
    display.refresh()
    time.sleep(2)
    main_screen.run_mainScreen(display)
    #login.save_user(name)

#display precedents name
def loadNames(display,group):
    noms_precedents = login.load_users()
    y_position = 100
    if noms_precedents:
        text_lastNames = label.Label(FONT, text="Noms precedents:", color=0xFFFFFF, x=125, y=y_position)
        group.append(text_lastNames)
        y_position += 20
        for nom in noms_precedents[-3:]:  # display the three last names
            text_name = label.Label(FONT, text=nom, color=0xFFFFFF, x=140, y=y_position)
            group.append(text_name)
            y_position += 15

#return the name and display it
#use the inputs to write
def writeName(display, group):
    input_text = ""
    max_length = 10  # max character allow
    while True:
        # input
        try:
            input_char = sys.stdin.read(1)

            if input_char in ['\r', '\n']:  # enter to stop
                break
            elif input_char == '\b':  #  backspace
                if len(input_text) > 0:
                    group.pop()
                input_text = input_text[:-1]
            elif input_char == '\x03':  # Ctrl+C to stop
                break
            elif len(input_text) >= max_length: # verify the limit
                break
            else:
                #add a character
                input_text+= input_char
                #display the text
                print(f"Texte entré : {input_text}")
                text_entree = label.Label(FONT, text=input_text, color=0xFFFFFF, x=160, y=80)
                group.append(text_entree)
            display.refresh()

            time.sleep(0.1)

        except KeyboardInterrupt:
            break
    return input_text

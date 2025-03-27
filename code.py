
import board
import busio
import displayio
import digitalio
import terminalio
import time
from adafruit_display_text import label
from fourwire import FourWire

from adafruit_st7789 import ST7789

# Release any resources currently in use for the displays
displayio.release_displays()

# Initialisation SPI
spi = busio.SPI(clock=board.GP18, MOSI=board.GP19)

# Utilisation de board.Pin au lieu de DigitalInOut
tft_cs = board.GP27  # Pin pour le chip select
tft_dc = board.GP21  # Pin pour le Data/Command

# Connexion SPI avec l'écran
display_bus = FourWire(spi, command=tft_dc, chip_select=tft_cs, reset=board.GP20)

# Initialisation de l'écran ST7789
display = ST7789(display_bus, width=320, height=240, rotation=90)

# Créer le groupe pour l'affichage
splash = displayio.Group()
display.root_group = splash

# Fond bleu sombre
color_bitmap = displayio.Bitmap(320, 240, 1)
color_palette = displayio.Palette(1)
color_palette[0] = 0x06024b  # Bleu sombre

bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
splash.append(bg_sprite)

# Dessiner un rectangle intérieur bleu
inner_bitmap = displayio.Bitmap(280, 200, 1)
inner_palette = displayio.Palette(1)
inner_palette[0] = 0x0B029C  # Bleu
inner_sprite = displayio.TileGrid(inner_bitmap, pixel_shader=inner_palette, x=20, y=20)
splash.append(inner_sprite)

# Ajouter du texte jaune
text_group = displayio.Group(scale=3, x=57, y=120)
text = "-Keycube-"
text_area = label.Label(terminalio.FONT, text=text, color=0xFFFFFF)
text_group.append(text_area)  # Sous-groupe pour le texte et l'échelle
splash.append(text_group)

# Configuration des boutons
button1 = digitalio.DigitalInOut(board.GP15)
button1.direction = digitalio.Direction.INPUT
button1.pull = digitalio.Pull.UP  # Bouton en pull-up

button2 = digitalio.DigitalInOut(board.GP14)
button2.direction = digitalio.Direction.INPUT
button2.pull = digitalio.Pull.UP  # Bouton en pull-up

# Boucle pour faire clignoter toutes les 3 secondes
while True:
    # 1. Changer les couleurs (fond et rectangle en rouge, texte en noir)
    color_palette[0] = 0x410000  # Fond rouge foncé
    inner_palette[0] = 0x8B0000  # Rectangle rouge foncé
    text_area.color = 0x000000    # Texte en noir
    display.refresh()
    time.sleep(3)
    
    # 2. Revenir aux couleurs d'origine (fond bleu, rectangle bleu, texte jaune)
    color_palette[0] = 0x06024b  # Bleu sombre
    inner_palette[0] = 0x0B029C  # Bleu
    text_area.color = 0xFFFFFF   # Texte jaune
    display.refresh()
    time.sleep(3)
    
    if button2.value:  # Appui sur bouton 2 et mode vert
        color_palette[0] = 0x01370a  # Vert sombre
        inner_palette[0] = 0x00da25  # Vert
        text_area.color = 0x000000   # Texte noir
        
        time.sleep(3)  # Débounce
        
    if button1.value:  # Appui sur bouton 2 et mode vert
        color_palette[0] = 0x62006a  # Violet sombre
        inner_palette[0] = 0xd700e8  # Violet
        text_area.color = 0xFFFFFF   # Texte jaune
        
        time.sleep(3)  # Débounce

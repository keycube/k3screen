import displayio
from adafruit_display_text import label
from adafruit_bitmap_font import bitmap_font
import time
def testFont(display):
    #create the group that we use to show something
    group = displayio.Group()
    display.root_group = group
    while True:
        # load a font
        font = bitmap_font.load_font("/fonts/LeagueSpartan-Bold-16.bdf")
        text_area = label.Label(font, text="test de la font:", color=0xFFFFFF, x=125, y=50)
        # erase the last thing in the group
        group.pop() if len(group) > 0 else None
        group.append(text_area)
        display.refresh()
        time.sleep(2)
        print("change")

        font = bitmap_font.load_font("/fonts/LibreBodoniv2002-Bold-27.bdf")
        text_area = label.Label(font, text="test de la font:", color=0xFFFFFF, x=125, y=50)
        group.pop() if len(group) > 0 else None
        group.append(text_area)
        display.refresh()
        time.sleep(2)
        print("change")

import board
import busio
import home
import ExImg
import ExFont
import displayio
import sharpdisplay
import framebufferio
import main_screen
import TestScroll
import sdcardio
import storage
import adafruit_sdcard
import digitalio

# --- Initialisation sdcard ---
spi = busio.SPI(clock=board.GP2, MOSI=board.GP3, MISO=board.GP4)
cs = digitalio.DigitalInOut(board.GP5)
sdcard = adafruit_sdcard.SDCard(spi, cs)
vfs = storage.VfsFat(sdcard)
storage.mount(vfs, "/sd")

# --- Initialisation SPI and screen ---
# Initialize the display, cleaning up after a display from the previous runif necessary
displayio.release_displays()
bus = busio.SPI(clock=board.GP10, MOSI=board.GP11)
framebuffer = sharpdisplay.SharpMemoryFramebuffer(bus, board.GP13, 400, 240)
display = framebufferio.FramebufferDisplay(framebuffer, auto_refresh = True)



# --- launching another file ---

#launch the app
#home.run_welcomeScreen(display)

#launch the ex to change font
#ExFont.testFont(display)

#launch the ex to display an image
#ExImg.run_imgTest(display)

#main_screen.run_mainScreen(display)

#TestScroll.run_Scroll(display)

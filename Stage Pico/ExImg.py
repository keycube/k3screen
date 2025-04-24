import displayio
import time
def run_imgTest(display):
    # load the bmp image
    image = displayio.OnDiskBitmap("dog.bmp")
    tile_grid = displayio.TileGrid(image, pixel_shader=getattr(image, 'pixel_shader', displayio.ColorConverter()))

    # create a display group
    group = displayio.Group()
    group.append(tile_grid)

    # display on screen
    display.root_group = group

    # keep it display
    while True:
        time.sleep(1)

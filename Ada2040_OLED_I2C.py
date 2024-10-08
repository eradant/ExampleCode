import time
import board
import busio
import displayio
import terminalio
from adafruit_display_text import label
import adafruit_displayio_ssd1306
import adafruit_ltr390

displayio.release_displays()

i2c = busio.I2C(board.SCL, board.SDA)
display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)
ltr = adafruit_ltr390.LTR390(i2c)


while True:

    # Make the display context
    text_group = displayio.Group()

    # Draw a label
    text = "ENVIRONMENT SENSOR"
    text_area = label.Label(terminalio.FONT, text=text, color=0xFFFFFF, x=10, y=4)
    text_group.append(text_area)

    text = "Ambient: {:.2f}".format(ltr.light)
    text_area = label.Label(terminalio.FONT, text=text, color=0xFFFFFF, x=10, y=20)
    text_group.append(text_area)
    
    text = "UV: {:.2f}".format(ltr.uvs)
    text_area = label.Label(terminalio.FONT, text=text, color=0xFFFFFF, x=10, y=36)
    text_group.append(text_area)
    
    text = "Lux: {:.2f}".format(ltr.lux)
    text_area = label.Label(terminalio.FONT, text=text, color=0xFFFFFF, x=10, y=54)
    text_group.append(text_area)

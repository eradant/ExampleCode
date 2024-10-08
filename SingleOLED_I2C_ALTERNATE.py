import time
import board
import busio as io
import adafruit_ssd1306


i2c = io.I2C(scl=board.GP3, sda=board.GP2)
display = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x3C)

while True:
    display.text("LIGHT INTENSITY", 15, 0, 1)
    display.show()
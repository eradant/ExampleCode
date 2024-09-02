import adafruit_ssd1306, board, busio

display_one = adafruit_ssd1306.SSD1306_I2C(128, 64, busio.I2C(scl=board.GP3, sda=board.GP2))

display_one.fill(0)
display_one.text("Display One", 30,12, True)
display_one.show()
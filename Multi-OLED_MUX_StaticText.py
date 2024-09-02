import adafruit_ssd1306, board, busio
import adafruit_tca9548a
import time

i2c = busio.I2C(scl=board.GP3, sda=board.GP2)

tca = adafruit_tca9548a.TCA9548A(i2c,address=0X70)

display_one = adafruit_ssd1306.SSD1306_I2C(128, 64, tca[2]) 

display_one.fill(0)
display_one.text("Display Three", 30,2, True)
display_one.text("Display Three", 30,50, True)
display_one.show()

display_two = adafruit_ssd1306.SSD1306_I2C(128, 64, tca[7]) 

display_two.fill(0)
display_two.text("Display two", 30,20, True)
display_two.show()

display_three = adafruit_ssd1306.SSD1306_I2C(128, 64, tca[6]) 

display_three.fill(0)
display_three.text("Display one", 30,20, True)
display_three.show()

display_four = adafruit_ssd1306.SSD1306_I2C(128, 64, tca[5]) 

display_four.fill(0)
display_four.text("Display four", 30,20, True)
display_four.show()
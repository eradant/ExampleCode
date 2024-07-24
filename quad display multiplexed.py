import adafruit_ssd1306, board, busio
import adafruit_tca9548a
import time
import adafruit_ltr390
from adafruit_dps310.basic import DPS310
import adafruit_sht4x



i2c = busio.I2C(scl=board.GP3, sda=board.GP2)

tca = adafruit_tca9548a.TCA9548A(i2c,address=0X70)

display_one = adafruit_ssd1306.SSD1306_I2C(128, 64, tca[2])
display_two = adafruit_ssd1306.SSD1306_I2C(128, 64, tca[7])
display_three = adafruit_ssd1306.SSD1306_I2C(128, 64, tca[6])
display_four = adafruit_ssd1306.SSD1306_I2C(128, 64, tca[5])
ltr = adafruit_ltr390.LTR390(tca[1])
dps310 = DPS310(tca[1])
sht30 = adafruit_sht4x.SHT4x(tca[1])

while True:
    

    display_one.fill(0)
    display_one.text("UV Sensor", 30,2, True)
    display_one.text("Ambient: {:.2f}".format(ltr.light), 30,18, True)
    display_one.text("UV: {:.2f}".format(ltr.uvs), 30,34, True)
    display_one.text("Lux: {:.2f}".format(ltr.lux), 30, 50, True)
    display_one.show()



    display_two.fill(0)
    display_two.text("Temp/Pressure", 30,2, True)
    display_two.text("T = %.2f *C" % dps310.temperature, 30,25, True)
    display_two.text("P = %.2f hPa" % dps310.pressure, 30,50, True)
    display_two.show()


    display_three.fill(0)
    display_three.text("Humidity/Temp", 30, 2, True)
    display_three.text("Humi(%):  {:.2f}".format(sht30.relative_humidity), 30,25, True)
    display_three.text("Temp(C):  {:.2f}".format(sht30.temperature), 30,50, True)
    display_three.show()



    display_four.fill(0)
    display_four.text("Display four", 30,2, True)
    display_four.text("Display four", 30,25, True)
    display_four.text("Display four", 30,50, True)
    display_four.show()
    
    time.sleep(1)


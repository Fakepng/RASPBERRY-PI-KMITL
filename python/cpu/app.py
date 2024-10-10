from RPLCD.i2c import CharLCD
from gpiozero import CPUTemperature
import time

lcd = CharLCD(i2c_expander='PCF8574', address=0x26, port=1, cols=16, rows=2, dotsize=8)
lcd.clear()

celcius = 0
celcius_bitmap = (
  0b11000,
  0b11000,
  0b00011,
  0b00100,
  0b00100,
  0b00100,
  0b00011,
  0b00000,
)
lcd.create_char(celcius, celcius_bitmap)

lcd.clear()
lcd.home()
lcd.write_string("CPU Temperature:")

while True:
  cpu = CPUTemperature()

  lcd.cursor_pos = (1,10)
  lcd.write_string("{0:.2f}".format(cpu.temperature))
  lcd.write(celcius)

  time.sleep(1.0)
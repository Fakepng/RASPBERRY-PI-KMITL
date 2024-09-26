from RPLCD.i2c import CharLCD
import time
import board
import adafruit_dht

dht = adafruit_dht.DHT11(board.D25)

lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1, cols=16, rows=2, dotsize=8)
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

percent = 1
percent_bitmap = (
  0b00000,
  0b00000,
  0b11001,
  0b11010,
  0b00100,
  0b01011,
  0b10011,
  0b00000,
)
lcd.create_char(percent, percent_bitmap)

lcd.clear()
lcd.write_string("Temperature:")
lcd.crlf()
lcd.write_string("Humidity:")

while True:
  try:
    temperature = dht.temperature
    humidity = dht.humidity

    lcd.cursor_pos = (0,13)
    lcd.write_string("{0:>}".format(temperature))
    lcd.write(celcius)

    lcd.cursor_pos = (1,13)
    lcd.write_string("{0:>}".format(humidity))
    lcd.write(percent)

  except RuntimeError as error:
    print(error.args[0])
    time.sleep(2.0)
    continue

  except Exception as error:
    dht.exit()
    raise error

  time.sleep(2.0)
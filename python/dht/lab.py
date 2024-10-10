from RPLCD.i2c import CharLCD
from gpiozero import Button
import time
import board
import adafruit_dht
import csv

dht = adafruit_dht.DHT11(board.D25)
btn = Button(26)

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

isDisplayTemp = False
lastTempUpdate = time.time() - 2000
filename = time.strftime("%Y%m%d%H%M%S") + "-Log.csv"

global temperature
global humidity

try:
  temperature = dht.temperature
  humidity = dht.humidity

except RuntimeError as error:
  print(error.args[0])
  time.sleep(2.0)

except Exception as error:
  dht.exit()
  raise error

with open(filename, "w", newline="") as file:
  writer = csv.writer(file)
  writer.writerow(["Date", "Time", "Temperature", "Humidity"])

  while True:
    if isDisplayTemp is True and btn.is_pressed:
      lcd.clear()
      lcd.write_string("Time:")
      lcd.crlf()
      lcd.write_string("Date:")
      isDisplayTemp = False

    if isDisplayTemp is False and not btn.is_pressed:
      lcd.clear()
      lcd.write_string("Temperature:")
      lcd.crlf()
      lcd.write_string("Humidity:")
      isDisplayTemp = True

    try:
      if time.time() - lastTempUpdate >= 2:
        temperature = dht.temperature
        humidity = dht.humidity

        writer.writerow([time.strftime("%m/%d/%Y"), time.strftime("%H:%M:%S"), temperature, humidity])

        lastTempUpdate = time.time()

    except RuntimeError as error:
      print(error.args[0])
      continue

    except Exception as error:
      dht.exit()
      raise error

    if not btn.is_pressed:
      lcd.cursor_pos = (0,13)
      lcd.write_string("{0:>}".format(temperature))
      lcd.write(celcius)

      lcd.cursor_pos = (1,13)
      lcd.write_string("{0:>}".format(humidity))
      lcd.write(percent)

    else:
      lcd.cursor_pos = (0, 7)
      lcd.write_string(time.strftime("%H:%M:%S"))
      lcd.cursor_pos = (1, 6)
      lcd.write_string(time.strftime("%d/%m/%Y"))

file.close()
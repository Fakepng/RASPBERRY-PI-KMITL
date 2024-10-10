from RPLCD.i2c import CharLCD
from gpiozero import Button
import time

lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1, cols=16, rows=2, dotsize=8, auto_linebreaks=False)
lcd.clear()

btn = Button(26)

korkai = 0
korkai_bitmap = (
  0b00000,
  0b00000,
  0b00110,
  0b01001,
  0b11001,
  0b01001,
  0b01001,
  0b00000
)
lcd.create_char(korkai, korkai_bitmap)

ruuu = 1
ruuu_bitmap = (
  0b00000,
  0b00000,
  0b00110,
  0b01001,
  0b01001,
  0b01001,
  0b01001,
  0b00001
)
lcd.create_char(ruuu, ruuu_bitmap)

ruusi = 2
ruusi_bitmap = (
  0b00000,
  0b00000,
  0b00000,
  0b11001,
  0b01011,
  0b01001,
  0b01111,
  0b00000
)
lcd.create_char(ruusi, ruusi_bitmap)

nainnn = 3
nainnn_bitmap = (
  0b00001,
  0b00010,
  0b01101,
  0b10101,
  0b10101,
  0b10111,
  0b11011,
  0b00000
)
lcd.create_char(nainnn, nainnn_bitmap)

malai = 4
malai_bitmap = (
  0b10100,
  0b01100,
  0b00100,
  0b00100,
  0b00100,
  0b00110,
  0b00110,
  0b00000
)
lcd.create_char(malai, malai_bitmap)

norrrnu = 5
norrrnu_bitmap = (
  0b00000,
  0b00000,
  0b11010,
  0b01010,
  0b01010,
  0b01111,
  0b01011,
  0b00000
)
lcd.create_char(norrrnu, norrrnu_bitmap)

taahann = 6
taahann_bitmap = (
  0b00001,
  0b00010,
  0b11011,
  0b01101,
  0b01001,
  0b01001,
  0b01001,
  0b00000
)
lcd.create_char(taahann, taahann_bitmap)

lcd.clear()
lcd.home()

krit = [0, 1, 2, 3]
night = [4, 5, 6]

shift = 0

while True:
  if shift > 15:
    shift = 0

  if shift < 0:
    shift = 15

  lcd.cursor_pos = (0, shift)
  for char in krit:
    lcd.write(char)

  lcd.cursor_pos = (1, shift)
  for char in night:
    lcd.write(char)

  if btn.is_pressed:
    shift -= 1
  else:
    shift += 1

  time.sleep(.5)
  lcd.clear()

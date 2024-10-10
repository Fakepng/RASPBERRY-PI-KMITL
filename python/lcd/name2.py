from RPLCD.i2c import CharLCD
from gpiozero import Button
import time

lcd = CharLCD(i2c_expander='PCF8574', address=0x26, port=1, cols=16, rows=2, dotsize=8, auto_linebreaks=False)
lcd.clear()

btn = Button(26)

korkai = 0
korkai_bitmap = (
  0x06,0x08,0x10,0x10,0x10,0x10,0x0E,0x06
)
lcd.create_char(korkai, korkai_bitmap)

ruuu = 1
ruuu_bitmap = (
  0x01,0x01,0x01,0x11,0x11,0x15,0x15,0x0A
)
lcd.create_char(ruuu, ruuu_bitmap)

ruusi = 2
ruusi_bitmap = (
  0x00,0x00,0x00,0x19,0x09,0x09,0x1F,0x1B
)
lcd.create_char(ruusi, ruusi_bitmap)

nainnn = 3
nainnn_bitmap = (
  0x0D,0x0E,0x00,0x1F,0x09,0x09,0x19,0x19
)
lcd.create_char(nainnn, nainnn_bitmap)

malai = 4
malai_bitmap = (
  0x00,0x00,0x00,0x19,0x0B,0x0D,0x09,0x09
)
lcd.create_char(malai, malai_bitmap)

norrrnu = 5
norrrnu_bitmap = (
  0x00,0x00,0x0D,0x12,0x08,0x04,0x02,0x0C
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

krit = [0, 1, 2]
night = [3, 4, 5]

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

from RPLCD.i2c import CharLCD

lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1, cols=16, rows=2, dotsize=8)
lcd.clear()

heart = (
  0b00000,
  0b01010,
  0b11111,
  0b11111,
  0b11111,
  0b01110,
  0b00100,
  0b00000,
)

lcd.create_char(0, heart)

lcd.write(0)
lcd.write_string("   66010375   ")
lcd.write(0)
lcd.crlf()
lcd.write(0)
lcd.write_string("   66011314   ")
lcd.write(0)

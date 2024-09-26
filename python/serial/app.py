import serial as Serial
import time

serial = Serial.Serial("/dev/ttyS0", 115200)

serial.write(str.encode("Hello Fakepng\r\n"))

while True:
  received_data = serial.read()
  time.sleep(0.03)
  data_left = serial.inWaiting()
  received_data += serial.read(data_left)

  print(received_data)
  serial.write(received_data)
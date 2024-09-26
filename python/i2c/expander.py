from smbus2 import SMBus
import time

bus_number = 1
bus = SMBus(bus_number)

for data in range(256):
  print("OUT: ", bin(data))
  bus.write_byte(0x25, data)
  time.sleep(.1)
  dataIn = bus.read_byte(0x25)
  print(" IN: ", bin(dataIn))
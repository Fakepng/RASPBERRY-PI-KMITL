from smbus2 import SMBus

bus_number = 1
bus = SMBus(bus_number)

for device in range(128):
  try:
    bus.read_byte(device)
    print(hex(device))
  except:
    print("[",hex(device),"]")
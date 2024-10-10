import time
import threading
import spidev
import random

bus = 0
device = 0

spi = spidev.SpiDev()
spi.open(bus, device)
spi.max_speed_hz = 50_000
spi.mode = 0

spi_fail_count = 0

def crc16_modbus(data: bytes) -> list:
    """Calculate the CRC16 Modbus checksum and return as a list of 2 bytes (MSB, LSB)."""
    crc = 0xFFFF
    for pos in data:
        crc ^= pos
        for _ in range(8):
            if crc & 0x0001:
                crc = (crc >> 1) ^ 0xA001
            else:
                crc >>= 1
    # Return as two bytes: MSB first, then LSB
    msb = (crc >> 8) & 0xFF  # Most significant byte
    lsb = crc & 0xFF         # Least significant byte
    return [msb, lsb]

def validate_crc16_modbus(data: bytes) -> bool:
    """Validate the CRC16 Modbus checksum for an 8-byte data packet."""
    if len(data) != 8:
        raise ValueError("Data packet must be 8 bytes long (6 data + 2 CRC).")

    # Split the data into payload (first 6 bytes) and CRC (last 2 bytes)
    payload = data[:-2]
    crc_received = list(data[-2:])  # Last two bytes as a list (MSB first)

    # Calculate the CRC16 on the first 6 bytes of the payload
    crc_calculated = crc16_modbus(payload)

    # Compare calculated CRC with the received CRC
    return crc_received == crc_calculated

def send_and_receive_spi(spi, n):
    global spi_fail_count
    global bus
    global device

    msg_int = [1, 1, 0, 0, 0] + [n]

    # Calculate CRC and send the message
    crc = crc16_modbus(msg_int)
    msg_crc = msg_int + crc
    print(f"Message with CRC: {msg_crc}")

    spi.xfer2(msg_crc)  # Send the message via SPI

    time.sleep(1)  # Optional delay

    # Read response
    received_data = spi.readbytes(8)
    print(f"Received data: {received_data}")

    # Validate received data CRC
    if validate_crc16_modbus(received_data):
        print("CRC validation passed.")
        spi_fail_count = 0
    else:
        print("CRC validation failed.")
        spi_fail_count = spi_fail_count + 1

        if (spi_fail_count >= 5):
            msg_int = [1, 1, 1, 0, 0, 0]
            crc = crc16_modbus(msg_int)
            msg_crc = msg_int + crc
            spi.xfer2(msg_crc)
            time.sleep(1)
            spi.close()
            time.sleep(1)
            spi.open(bus, device)





# Start SPI communication
while True:
  i = random.randint(0, 31)
  send_and_receive_spi(spi, i)
  time.sleep(.1)
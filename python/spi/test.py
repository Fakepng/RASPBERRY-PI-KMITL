import time
import threading
import spidev

bus = 0
device = 0

spi = spidev.SpiDev()
spi.open(bus, device)
spi.max_speed_hz = 50_000
spi.mode = 0

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

def send_and_receive_spi(spi):
    try:
        while True:
            msg = input("SPI (enter 6 values): ").split()

            # Check if input is valid
            try:
                msg_int = [int(i) for i in msg if i.isdigit()]
                if len(msg_int) != 6:
                    raise ValueError("Exactly 6 data bytes are required.")
            except ValueError as e:
                print(f"Invalid input: {e}")
                continue

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
            else:
                print("CRC validation failed.")

    except KeyboardInterrupt:
        print("Program interrupted, closing SPI...")
    finally:
        spi.close()

# Start SPI communication
send_and_receive_spi(spi)
import machine
from machine import Pin
PIN_D = (16, 5, 4, 0, 2, 14, 12, 13, 15)

spi = machine.SPI(1, baudrate=10000, polarity=0, phase=0)
spi.init()
cs = Pin(PIN_D[2], mode=Pin.OUT, value=1)      # Create chip-select on pin 4.

try:
    cs(0)                               # Select peripheral.
    spi.write(b"12345678")              # Write 8 bytes, and don't care about received data.
finally:
    cs(1)                               # Deselect peripheral.

try:
    cs(0)                               # Select peripheral.
    rxdata = spi.read(8, 0x42)          # Read 8 bytes while writing 0x42 for each byte.
    print(rxdata)
finally:
    cs(1)                               # Deselect peripheral.

rxdata = bytearray(8)
try:
    cs(0)                               # Select peripheral.
    spi.readinto(rxdata, 0x42)          # Read 8 bytes inplace while writing 0x42 for each byte.
finally:
    cs(1)                               # Deselect peripheral.

txdata = b"12345678"
rxdata = bytearray(len(txdata))
try:
    cs(0)                               # Select peripheral.
    spi.write_readinto(txdata, rxdata)  # Simultaneously write and read bytes.
finally:
    cs(1)                               # Deselect peripheral.
print(rxdata)
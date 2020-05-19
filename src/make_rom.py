"""
Usage: python make_rom.py

Inspect output: hexdump -C rom.bin

Write to EEPROM: minipro -p AT28C256 -w rom.bin
"""


rom = bytearray([0xEA] * 32768)

with open("rom.bin", "wb") as out_file:
    out_file.write(rom)

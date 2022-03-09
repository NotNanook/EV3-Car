# Bluetooth MAC Address EV3: 00:17:E9:B1:DF:9C
# get own address via hciconfig --all (Linux)
# get devices: 1. bluetoothctl 2. scan on (Linux)
"""
A simple Python script to send messages to a sever over Bluetooth
using PyBluez (with Python 2).
"""

import bluetooth

serverMACAddress = 'F8:E6:1A:80:00:BE'
port = 3
s = bluetooth.BluetoothSocket(bluetooth.L2CAP)
s.connect((serverMACAddress, port))
while 1:
    text = input() # Note change to the old (Python 2) raw_input
    if text == "quit":
        break
    s.send(text)
s.close()


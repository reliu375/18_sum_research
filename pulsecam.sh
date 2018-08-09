#!/bin/bash

# change permission of the ttyUSB0
sudo chmod 777 /dev/ttyUSB1

# initialize the lens
python3.5 test_usb.py

# run the program
# python3.5 focaltrack.py

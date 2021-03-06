#!/bin/bash

printf "**** Installing Adafruit_DHT Python package... ****\n"
sudo apt-get update
sudo apt-get install python3-pip
sudo python3 -m pip install --upgrade pip setuptools wheel
sudo pip3 install Adafruit_DHT
printf "**** Done. ****\n\n\n"

printf "**** Installing python-tsl2591 Python package... ****\n"
git clone https://github.com/maxlklaxl/python-tsl2591.git
sudo apt-get install libffi-dev
cd python-tsl2591
sudo python3 setup.py install
printf "**** Done. ****\n\n\n"

printf "**** Installing pandas and matplotlib Python packages... ****"
sudo pip3 install pandas matplotlib
printf "**** Done. ****\n\n\n"


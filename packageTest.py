#!/usr/bin/env python3

from GMPi_Pack import Sense
from GMPi_Pack import UploadFile
from GMPi_Pack import PicSnap
from GMPi_Pack import LightAlert
from GMPi_Pack import ReadConfig

config = ReadConfig()
filepath = config["output_path"]
rcloneProfile = config["rclone_profile"]
whichDHT = config["which_dht"]
whichDataPin = config["which_data_pin"]
minLight = config["minimum_light_threshold"]
maxLight = config["maximum_light_threshold"]

print( "Light Perameters Set")
print('Max is: {}'.format(maxLight))
print('Min is: {}'.format(minLight))
#OpenFile(filepath)

#sense also returns current light intensity value, possiably others in the future.
currentLight = Sense(filepath, whichDHT, whichDataPin)

if (currentLight < minLight or currentLight > maxLight):
   LightAlert()
   print('LightAlert sent')
#UploadFile(filepath, rcloneProfile)
#PicSnap(filepath, rcloneProfile)


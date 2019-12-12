# -*- coding: utf-8 -*-
"""
Created on Mon September 23 11:14:45 2019

@author: EsuaEkpo

@decription: This is the main entry point for run the autonomoous mission software module

"""

# http://127.0.0.1:5000/sensor_data/sensorID_01/lat_47.398039859999997/lon_8.5455725400000002/alt_2.00/state_HIGH

import time, sys, asyncio

from sensorListener import Listener
from utilities.parser import Parser
from sensorAuditor import Auditor
from sensor import Sensor
import mission, new

JUST_TAKEOFF_AND_LAND = 0

#instantiate the parser class
parser = Parser()

#instantiate the listener class
listen = Listener()

#instantiate the auditor class
audit = Auditor()

#add the parser class as a subscriber to the listener class so as to get update on sensor data from the 
#network
listen.add(parser)

#add the auditor class as a listener to the parser class so as  to recieve parsed and preprocessed sensor data
parser.add(audit)

#start up the network listener
listen.runListener()

#  for testing of the sensor module please comment this out (the while loop below)
while (True):
    time.sleep(1)
    if audit.mission:
        sensor = audit.mission
        print(f"********** {sensor} **********")
        sensor_position = sensor.position
        if JUST_TAKEOFF_AND_LAND:
            takeOffTime = 30
            new.run(takeOffTime)
        else:
            mission.run(sensor_position.latitude, sensor_position.longitude, sensor_position.altitude)
        break

audit.sensors

input()

#shutdown the listener
listen.shutdown_server()

#exit main thread this shuts down the listener thread as well
sys.exit()
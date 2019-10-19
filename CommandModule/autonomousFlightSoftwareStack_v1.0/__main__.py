# -*- coding: utf-8 -*-
"""
Created on Mon September 23 11:14:45 2019

@author: EsuaEkpo

@decription: This is the main entry point for run the autonomoous mission software module

"""
import time, sys, asyncio

from sensorListener import Listener
from utilities.parser import Parser
from sensorAuditor import Auditor
from sensor import Sensor
import mission

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

while (True):
    time.sleep(1)
    if audit.mission:
        sensor = audit.mission
        print(f"********** {sensor} **********")
        sensor_position = sensor.position
        asyncio.get_event_loop().run_until_complete(mission.runMission(sensor_position.latitude, sensor_position.longitude, sensor_position.altitude))
        break

audit.sensors

#shutdown the listener
listen.shutdown_server()

#exit main thread this shuts down the listener thread as well
sys.exit()
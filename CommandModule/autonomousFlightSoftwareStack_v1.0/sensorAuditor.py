# -*- coding: utf-8 -*-
"""
Created on Sat September 28 11:14:45 2019

@author: EsuaEkpo

@decription: This class keeps track of sensor objects communicating over the network,
monitoring of their states with a simple algorithm in order to ascertain if it has been triggered.
It is mean't to subcribe to the Parser class in order to be notified when new
sensor information is available, therefore it implements the 'notify()' method

"""

from sensor import Sensor

class Auditor(object):

    def __init__(self):
        self._sensors = []

    @property
    def sensors(self):
        return self._sensors
    
    def addSensor(self, sensor):
        if sensor not in self._sensors:
            self._sensors.append(sensor)

    def notify(self, publisher):
        print('Parsed payload recieved from Parser publisher into the Auditor.')
        sensorID = publisher.sensorID
        lat = publisher.latitude
        lon = publisher.longitude
        alt = publisher.altitude
        state = publisher.state

        sensor = 
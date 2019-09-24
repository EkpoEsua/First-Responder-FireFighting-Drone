# -*- coding: utf-8 -*-
"""
Created on Mon September 23 11:14:45 2019

@author: EsuaEkpo

@decription: This class encapsulates the properties of a sensor module as an object

"""

from utilities.location import Location

class Sensor(object):

    sensorID = 0

    def __init__(self, latitude, longitude, height=0):
        self._latitude = latitude
        self._longitude = longitude
        self._status = 0
        Sensor.sensorID += 1
        self._sensorId = Sensor.sensorID
        
    def getLocation(self):
        return 
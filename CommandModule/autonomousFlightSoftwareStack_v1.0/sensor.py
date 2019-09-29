# -*- coding: utf-8 -*-
"""
Created on Mon September 23 11:14:45 2019

@author: EsuaEkpo

@decription: This class encapsulates the properties of a sensor module as an object
for use by other modules

"""

from utilities.location import Location

class Sensor(object):

    def __init__(self, ID, latitude, longitude, altitude=0):
        self._location = Location(latitude, longitude)
        self._status = 'LOW'
        self._sensorId = ID
        
    """ 
    @requires: 
    @modifies:
    @returns: location object
    """
    def getLocation(self):
        return self._location

    """ 
    @requires: 
    @modifies:
    @returns: sensor ID tag
    """
    def getSensorID(self):
        return self._sensorId

    """ 
    @requires: 
    @modifies:
    @returns: status of the sensor -
    0: LOW
    1: HIGH
    """
    def getStatus(self):
        return self._status

    """ 
    @requires: the state of the sensor
    0: LOW
    1: HIGH
    @modifies: the status of the sensor
    @returns: 
    """
    def setStatus(self, state):
        self._status = state

    """ 
    @requires: 
    @modifies: overides the equals method from it parent class 'object' when checking if
    two sensors are the same, the property being checked for and compared is the
    sensorID since each sensor is expected to have a unique ID
    @returns:
    """
    def __eq__(self, sensor):
        
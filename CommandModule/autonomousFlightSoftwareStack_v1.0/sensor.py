# -*- coding: utf-8 -*-
"""
Created on Mon September 23 11:14:45 2019

@author: EsuaEkpo

@decription: This class encapsulates the properties of a sensor module as an object
for use by other modules such as the sensorAuditor

C:\\Users\\Esua Ekpo\\Documents\\Project First Responder Drone\\First-Responder-FireFighting-Drone\\CommandModule\\autonomousFlightSoftwareStack_v1.0\\utilities

"""
import sys

sys.path.append('C:\\Users\\Esua Ekpo\\Documents\\Project First Responder Drone\\First-Responder-FireFighting-Drone\\CommandModule\\autonomousFlightSoftwareStack_v1.0')

from utilities.location import Position

class Sensor(object):

    """ 
    @requires:  ID - string: latitude - double: longitude - double: altitude - double
    @modifies:
    @returns: creates sensor object
    """
    def __init__(self, ID, latitude, longitude, altitude=0):
        self._position = Position(latitude, longitude, altitude)
        self._state = ['LOW', 'LOW', 'LOW', 'LOW', 'LOW']
        self._sensorID = ID
        
    """ 
    @requires: 
    @modifies:
    @returns: position object
    """
    @property
    def position(self):
        return self._position

    """ 
    @requires: 
    @modifies:
    @returns: sensor ID tag
    """
    @property
    def sensorID(self):
        return self._sensorID

    """ 
    @requires: 
    @modifies:
    @returns: state of the sensor - this is represented as an array of 5 elements
    each element representing a read state of the sensor, this allows for mitigating a false positive
    situation in which several(5 in this case) consecutive readings are required to validate the true
    state of the sensor, in otherwords it serves as filter.
    'LOW': 0
    'HIGH': 1
    """
    @property
    def state(self):
        return self._state

    """ 
    @requires: the state of the sensor as a string
    0: 'LOW'
    1: 'HIGH'
    @modifies: the state of the sensor, it does this by inserting the newly
    recorded state at first position and removes the state from the end, this corresponds 
    to the oldest read value in a window of 5(five), this is synonymous to a push operation
    @returns: 
    """
    @state.setter
    def state(self, state):
        self._state.insert(0, state)
        self._state.pop()

    """ 
    @requires: 
    @modifies: checks the _state attribute of the sensor and return true if all
    elements of the attributes array is 'HIGH'
    @returns: bool: if sensor is triggered
    """
    @property
    def triggered(self):
        return self._state.count('HIGH') == 5

    """ 
    @requires: a sensor object
    @modifies: overides the equals method from it parent class 'object' when checking if
    two sensors are the same, the property being checked for and compared is the
    sensorID since each sensor is expected to have a unique ID
    @returns:
    """
    def __eq__(self, sensor):
        return self.sensorID == sensor.sensorID

    def __str__(self):
        return ('SensorID: {} - Latitude: {} - Longitude: {} - Altitude: {} - Triggered: {}'.format(self.sensorID, self.position.latitude, self.position.longitude, self.position.altitude, self.triggered))


#create sensor object for testing of the class only should be commented out
sensor1 = Sensor('01', 3.435, 98.234, 2.00)
sensor2 = Sensor('02', 4.435, 99.234, 3.00)
sensor3 = Sensor('03', 5.435, 97.234, 4.00)
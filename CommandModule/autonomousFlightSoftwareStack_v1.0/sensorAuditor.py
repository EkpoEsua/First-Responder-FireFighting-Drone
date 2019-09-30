# -*- coding: utf-8 -*-
"""
Created on Sat September 28 11:14:45 2019

@author: EsuaEkpo

@decription: This class keeps track of sensor objects communicating over the network,
monitoring of their states with a simple algorithm in order to ascertain if it has been triggered.
It is mean't to subcribe to the Parser class in order to be notified when new
sensor information is available, therefore it implements the 'notify()' method

"""

import sys

sys.path.append('C:\\Users\\Esua Ekpo\\Documents\\Project First Responder Drone\\First-Responder-FireFighting-Drone\\CommandModule\\autonomousFlightSoftwareStack_v1.0')

from sensor import Sensor
from utilities.publisher import Publisher

class Auditor(Publisher):

    def __init__(self):
        super().__init__(self)
        self._sensors = []

    @property
    def sensors(self):
        for sensor in self._sensors:
            print(sensor)

    """ 
    @requires: sensor: object, state: string ('HIGH' or 'LOW')
    @modifies: updates the sensor catalog, and add a sensor if it is new or it updates the sensor's state
    after updating a newly read state it checks if the sensor is in a triggered state, and the
    calls the notify method of its parent class so as to notify observers to take designated actions
    in this case the mission module
    @returns:
    """
    def updateSensors(self, sensor, state):
        if sensor not in self._sensors:
            print('Adding New sensor: {}'.format(sensor))
            self._sensors.append(sensor)
            sensor.state = state
        else:
            sensor.state = state
            print('Updated Sensor: {}'.format(sensor))
            if sensor.triggered:
                print('Notifying subscribers to the sensor\'s triggered state feed from the Auditor')
                super().notify()

    """ 
    @requires: 
    @modifies: called when the Parser class which it is subscribed to has parsed sensor data
    @returns:
    """
    def notify(self, publisher):
        print('Parsed payload recieved from Parser publisher into the Auditor.')
        sensorID = publisher.sensorID
        lat = publisher.latitude
        lon = publisher.longitude
        alt = publisher.altitude
        state = publisher.state
        self.updateSensors(Sensor(sensorID, lat, lon, alt), state)

    def __str__(self):
        return 'Auditor Class'

#create sensor object for testing of the class only should be commented out
audit = Auditor()
sensor1 = Sensor('01', 3.435, 98.234, 2.00)
sensor2 = Sensor('02', 4.435, 99.234, 3.00)
sensor3 = Sensor('03', 5.435, 97.234, 4.00)
sensor4 = Sensor('04', 6.435, 96.234, 5.00)
sensor5 = Sensor('05', 7.435, 94.234, 6.00)
sensor6 = Sensor('06', 8.435, 92.234, 7.00)
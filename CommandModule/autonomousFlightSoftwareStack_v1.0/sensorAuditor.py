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
from utilities.publisher import Publisher

class Auditor(object):

    def __init__(self):
        # super().__init__(self)
        self._sensors = []
        self._missionAvailable = False
        self._triggeredSensor = None

    @property
    def sensors(self):
        for sensor in self._sensors:
            print(sensor)

    @property
    def mission(self):
        """
        Contains mission information for triggered sensor
        """

        if self._missionAvailable:
            return self._triggeredSensor
        else:
            return False

    @mission.setter
    def mission(self, sensor):
        """
        Sets the _triggered sensor attribute to the trigerred sensor
        """

        if not self._missionAvailable:
            print('Activating mission tracker and setting triggerred sensor')
            self._triggeredSensor = sensor
            self._missionAvailable = True

    def updateSensors(self, sensor, state):
        """ 
        @requires: sensor: object, state: string ('HIGH' or 'LOW')
        @modifies: updates the sensor catalog, and add a sensor if it is new or it updates the sensor's state
        after updating a newly read state it checks if the sensor is in a triggered state, and the
        calls the notify method of its parent class so as to notify observers to take designated actions
        in this case the mission module
        @returns:
        """


        if sensor not in self._sensors:
            print('Adding New sensor: {}'.format(sensor))
            self._sensors.append(sensor)
            sensor.state = state
        else:
            sensor = self._sensors[self._sensors.index(sensor)]
            sensor.state = state
            print(sensor.state)
            print('Updated Sensor: {}'.format(sensor))
            if sensor.triggered:
                # super().notify()
                self.mission = sensor
    
    def notify(self, publisher):
        """ 
        @requires: 
        @modifies: called when the Parser class which it is subscribed to has parsed sensor data
        @returns:
        """


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
# audit = Auditor()
# sensor1 = Sensor('01', 3.435, 98.234, 2.00)
# sensor2 = Sensor('02', 4.435, 99.234, 3.00)
# sensor3 = Sensor('03', 5.435, 97.234, 4.00)
# sensor4 = Sensor('04', 6.435, 96.234, 5.00)
# sensor5 = Sensor('05', 7.435, 94.234, 6.00)
# sensor6 = Sensor('06', 8.435, 92.234, 7.00)
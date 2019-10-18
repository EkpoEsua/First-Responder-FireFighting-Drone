
"""
Created on Thursday September 26 11:14:45 2019

@author: EsuaEkpo

@decription: This class implements a string parser that takes in string sensor data
from the Listener class in its payload and creates attributes relatiing to sesnor data
such as an ID, latitude, longitude, state and altitude attribute within its instance, 
this attributes will be used to create a sensor object having such attributes.

"""
import sys

print(sys.path[0])

from  utilities.publisher import Publisher

class Parser(Publisher):

    def __init__(self):
        super().__init__(self)
        self._payload = ''
        self._cabins = []
        self._sensorID = ''
        self._latitude = 0.0
        self._longitude = 0.0
        self._altitude = 0.0
        self._state = ''

    """ 
    @requires:
    @modifies: makes the payload available as an attribute using the @property decorator
    @returns:
    """
    @property
    def payload(self):
        return self._payload

    """ 
    @requires: a new payload string 
    @modifies: sets the class attribute _payload to the passed in string using the
    '=' assingment operator. It also calls the parsePayload Method
    @returns:
    """
    @payload.setter
    def payload(self, new_payload):
        try:
            print('about to assign payload in Parser')
            self._payload = new_payload
            self.parsePayload()
        except ValueError as e:
            print('Error: {}'.format(e))
        else:
            print("notifying publisher class from Parser class")
            super().notify()

    @property
    def sensorID(self):
        return self._sensorID
    
    @sensorID.setter
    def sensorID(self, id):
        self._sensorID = id

    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, lat):
        self._latitude = lat

    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, lon):
        self._longitude = lon

    @property
    def altitude(self):
        return self._altitude

    @altitude.setter
    def altitude(self, alt):
        self._altitude = alt

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state):
        self._state = state

    """ 
    @requires:
    @modifies:
    @returns: ID data from the cabin
    """
    def getID(self):
        info = self._cabins[0]
        data = self.findData(info)
        return data

    """ 
    @requires:
    @modifies:
    @returns: latitude data from the cabin
    """
    def getLatitude(self):
        info = self._cabins[1]
        data = self.findData(info)
        data = float(data)
        return data

    """ 
    @requires:
    @modifies:
    @returns: longitude data from the cabin
    """
    def getLongitude(self):
        info = self._cabins[2]
        data = self.findData(info)
        data = float(data)
        return data

    """ 
    @requires:
    @modifies:
    @returns: altitude data from the cabin
    """
    def getAltitude(self):
        info = self._cabins[3]
        data = self.findData(info)
        data = float(data)
        return data

    """ 
    @requires:
    @modifies:
    @returns: state data from the cabin
    """
    def getState(self):
        info = self._cabins[4]
        data = self.findData(info)
        return data

    """ 
    @requires:
    @modifies:creates an array of 'cabin' sectionized payload seperated
    by hyphens '-'
    @returns: 
    """
    def parsePayload(self):
        print('Parsing sensor data in Parser...')
        self._cabins = self._payload.split('-')
        self.sensorID = self.getID()
        self.latitude = self.getLatitude()
        self.longitude = self.getLongitude()
        self.altitude = self.getAltitude()
        self.state =  self.getState()
        print('Parsing done!')
        print('Data gotten')
        print('SensorID: {} - Latitude: {} - Longitude: {} - Altitude: {} - State: {}'.format(self.sensorID, self.latitude, self.longitude, self.altitude, self.state))

    """ 
    @requires: a raw chunk of sensor data segment
    @modifies:
    @returns: the main data in the string know as the "data"
    e.x. raw = "lon_30.94"
         data = "30.94"
    """
    def findData(self, raw):
        data = ''
        index = raw.find('_')
        data = raw[index+1:]
        return data

    
    def notify(self, publisher):
        print ('notification from publisher into Parser class')
        self.payload = publisher.payload
        print('payload gotten from publisher')

    def __str__(self):
        return 'Parser Class'

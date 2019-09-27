# -*- coding: utf-8 -*-
"""
Created on Thursday September 26 11:14:45 2019

@author: EsuaEkpo

@decription: This class implements a string parser that takes in string sensor data
from the Listener class in its payload and creates attributes relatiing to sesnor data
such as an ID, latitude, longitude, state and altitude attribute within its instance, 
this attributes will be used to create a sensor object having such attributes.

"""


class Parser(object):

    payload = "sensorID_01-lat_20.23-lon_30.23-alt_0.00-state_HIGH"
    cabins = []

    """ 
    @requires:
    @modifies:
    @returns: ID data from the cabin
    """
    def getID(self):
        info = Parser.cabins[0]
        data = self.findData(info)
        return data

    """ 
    @requires:
    @modifies:
    @returns: latitude data from the cabin
    """
    def getLatitude(self):
        info = Parser.cabins[1]
        data = self.findData(info)
        data = float(data)
        return data

    """ 
    @requires:
    @modifies:
    @returns: longitude data from the cabin
    """
    def getLongitude(self):
        info = Parser.cabins[2]
        data = self.findData(info)
        data = float(data)
        return data

    """ 
    @requires:
    @modifies:
    @returns: altitude data from the cabin
    """
    def getAltitude(self):
        info = Parser.cabins[3]
        data = self.findData(info)
        data = float(data)
        return data

    """ 
    @requires:
    @modifies:
    @returns: state data from the cabin
    """
    def getState(self):
        info = Parser.cabins[4]
        data = self.findData(info)
        return data

    """ 
    @requires:
    @modifies:creates an array of 'cabin' sectionized payload seperated
    by hyphens '-'
    @returns: 
    """
    def parsePayload(self):
        Parser.cabins = Parser.payload.split('-')

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

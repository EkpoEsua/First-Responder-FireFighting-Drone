"""
Created on Mon September 23 11:14:45 2019

@author: EsuaEkpo

@decription: This class specifies the GPS location of an object in latitude and longitude

"""

class Location(object):

    def __init__(self, latitude, longitude):
        self._latitude = latitude
        self._longitude = longitude

    """ 
    @requires: 
    @modifies:
    @returns: latitude double
    """
    def getLatitude(self):
        return self._latitude

    """ 
    @requires: 
    @modifies:
    @returns: longitude
    """
    def getLongitude(self):
        return self._longitude
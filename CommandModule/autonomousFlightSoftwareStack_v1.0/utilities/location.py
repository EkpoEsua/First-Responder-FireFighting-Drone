"""
Created on Mon September 23 11:14:45 2019

@author: EsuaEkpo

@decription: This class specifies the GPS location of a sensor in latitude and longitude
as well as its altitude
"""

class Position(object):

    def __init__(self, latitude, longitude, altitude=0):
        self._latitude = latitude
        self._longitude = longitude
        self._altitude = altitude

    """ 
    @requires: 
    @modifies:
    @returns: latitude - double
    """
    @property
    def latitude(self):
        return self._latitude

    """ 
    @requires: 
    @modifies:
    @returns: longitude - double
    """
    @property
    def longitude(self):
        return self._longitude

    """ 
    @requires: 
    @modifies:
    @returns: altitude - double
    """
    @property
    def altitude(self):
        return self._altitude
# -*- coding: utf-8 -*-
"""
Created on Friday September 27 11:14:45 2019

@author: EsuaEkpo

@decription: This class is a publisher that publishes the Parser class info to subscribers
of which is the SensorAudit class

"""

class Publisher():

    def __init__(self):
        self.observers = []

    """ 
    @requires: observe object
    @modifies: adds an observer object to the array of observers to subcribe to a publisher
    @returns:
    """
    def add(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)
        else:
            print('Faile to add: {}'.format(observer))

    """ 
    @requires: observer object
    @modifies: removes the passed in observer object from the array of observers
    @returns:
    """
    def remove(self, observer):
        try:
            self.observers.remove(observer)
        except ValueError:
            print('Failed to remove: {}'.format(observer))

    """ 
    @requires:
    @modifies: notifies subcribed observers of a newly published message by the publishers
    @returns:
    """
    def notify(self):
        for o in self.observers:
            o.notify(self)


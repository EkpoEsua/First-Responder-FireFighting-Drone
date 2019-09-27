# -*- coding: utf-8 -*-
"""
Created on Mon September 23 11:14:45 2019

@author: EsuaEkpo

@decription: This class listens for sensor messages over the network, sent using
html protocol, it makes use of the Flask framework and offloads this information
into the parser class for further processing.

"""

from flask import Flask
import threading
from utilities.parser import Parser


class Listener(object):

    listener = Flask(__name__)

    def __init__(self):
        
        # register url and callback function by which sensors offload their data
        Listener.listener.add_url_rule("/sensor_data/<string:id>/<string:lat>/<string:lon>/<string:alt>/<string:state>", "index", self.index)

        # create a thread to run network listener and register associated method to run it
        self.thread = threading.Thread(target=self.runListenerOnThread)

        #set the thread daemon as True so that the thread is closed on exit of main thread
        self.thread.daemon = True

    """ 
    @requires:
    @modifies:
    @returns: ID data from the cabin
    """
    def index(self, id, lat, lon, alt, state):
        dash = "-"
        payload = id+dash+lat+dash+lon+dash+alt+dash+state
        Parser.payload = payload
        print(payload)
        return "OK"

    """ 
    @requires:
    @modifies: starts the thread that runs network listener
    @returns:
    """
    def runListener(self):
        self.thread.start()

    """ 
    @requires:
    @modifies: runs network listener using the Flask.run()
    method exposed to the network as host - '0.0.0.0'
    on port: 5000
    @returns:
    """  
    def runListenerOnThread(self):
        Listener.listener.run(host='0.0.0.0', port=5000)
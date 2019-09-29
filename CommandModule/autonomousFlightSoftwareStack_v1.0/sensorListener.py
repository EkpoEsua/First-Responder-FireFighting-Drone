# -*- coding: utf-8 -*-
"""
Created on Mon September 23 11:14:45 2019

@author: EsuaEkpo

@decription: This class listens for sensor messages over the network, sent using
html protocol, it makes use of the Flask framework and offloads this information
into the parser class for further processing.

The network listener is run on a seperate thread from the main thread so as to allow
for concurrent listening over the network and performing other tasks on the main
thread.

"""

from flask import Flask, request
import threading, time
from utilities.publisher import Publisher


class Listener(Publisher):

    

    def __init__(self):

        super().__init__()

        self._listener = Flask(__name__)
        self._stop = False
        self._continue = False
        self._payload = ''
        
        # register url and callback function by which sensors offload their data
        self._listener.add_url_rule("/sensor_data/<string:id>/<string:lat>/<string:lon>/<string:alt>/<string:state>", "index", self.index)

        # create a thread to run network listener and register associated method to run it
        self._thread = threading.Thread(target=self.runListenerOnThread)

        #set the thread daemon as True so that the thread is closed on exit of main thread
        self._thread.daemon = True

    @property
    def payload(self):
        return self._payload

    @payload.setter
    def payload(self, new_payload):
        try:
            print('Loading payload in Listener')
            self._payload = new_payload
        except ValueError as e:
            print('Error: {}'.format(e))
        else:
            print('notifying publisher class from Listener')
            self.notify()

    """ 
    @requires: sensor information, its (id, latitude, longitude, altitude, and state)
    @modifies: loads sent sensor data into Parser payload attribute for further processing
    @returns: sends an 'OK' message back to sensor module in event of sucessfully loading sent data
    or 'OFF' when the server has been shutdown
    """
    def index(self, id, lat, lon, alt, state):
        self._continue = True
        if self._stop:
            # routine for shutting down listener
            func = request.environ.get('werkzeug.server.shutdown')
            if func:
                func()
            
            #wait for server to shutdown
            print('waiting for listener to shutdown...')
            time.sleep(10)
            print('listener shutdown!')
            return "OFF"
        else:
            dash = "-"
            payload = id + dash + lat + dash + lon + dash + alt + dash + state
            self.payload = payload
            print(payload)
            return "OK"

    """ 
    @requires:
    @modifies: starts the thread that runs network listener
    @returns:
    """
    def runListener(self):
        self._thread.start()

    """ 
    @requires:
    @modifies: runs network listener using the Flask.run()
    method exposed to the network as host - '0.0.0.0'
    on port: 5000
    @returns:
    """  
    def runListenerOnThread(self):
        self._listener.run(host='0.0.0.0', port=5000)

    """ 
    @requires:
    @modifies: set stop variable to true so as to initiate shuttingdown of the server
    @returns:
    """
    def shutdown_server(self):
        self._stop = True
        print('Listener shutdown intiated!')
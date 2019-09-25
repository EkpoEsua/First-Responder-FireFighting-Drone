# -*- coding: utf-8 -*-
"""
Created on Mon September 23 11:14:45 2019

@author: EsuaEkpo

@decription: This class listens for sensor messages over the network, sent using
html protocol, it makes use of the Flask framework.

"""

from flask import Flask, request


class Listener(object):

    listener = Flask(__name__)

    def __init__(self):
        Listener.listener.add_url_rule("/", "index", self.index)
        # Listener.listener.add_url_rule('/stop', 'shutdown', self.shutdown)

    def index(self):
        print('hello')
        return ""

    # def shutdown(self):
    #     print ('Listener is shutting down')
    #     self.shutdownListener()
    #     return ""

    def shutdownListener(self):
        func = request.environ.get('werkzeug.server.shutdown')
        if func is None:
            raise RuntimeError('Not running with the Werkzeug Server')
        func()

    def runListener(self):
        Listener.listener.run()
    